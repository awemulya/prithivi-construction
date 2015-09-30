import datetime
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from inventory.models import Category, Item, InventoryAccount, Demand, DemandRow, Party, Purchase, PurchaseRow, \
    set_transactions, DEFAULT_PROJECT_ID, ConsumptionRow, PartyPayment
from ledger.models import Account, set_transactions as set_ledger_transactions
from project.models import Project


class CategorySerializer(ModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent.name')

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'parent', 'parent_name')


class ItemSerializer(serializers.ModelSerializer):
    account_no = serializers.CharField(source='account.account_no')
    # site_id = serializers.CharField(source='account.site.id')
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all())
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = ('id', 'code', 'name', 'description', 'category_name', 'type', 'unit', 'account_no', 'category_id',
                  )

    def create(self, validated_data):
        account_no = validated_data.pop('account').get('account_no')
        # site_id = validated_data.pop('site').get('id')
        item = Item.objects.create(**validated_data)
        # if not site_id:
        #     site_id = DEFAULT_PROJECT_ID
        site_id = DEFAULT_PROJECT_ID

        if account_no:
            if item.account:
                account = item.account
                if InventoryAccount.objects.filter(account_no=account_no).exists():
                    account_no = int(account_no) +1
                account.account_no = account_no
                account.save()
            else:
                account = InventoryAccount(name=item.name, account_no=account_no, site_id=site_id)
                account.save()
                item.account = account
        item.save()
        return item

    def update(self, instance, validated_data):
        item = Item.objects.get(pk=instance.id)
        item.code = validated_data.pop('code')
        item.name = validated_data.pop('name')
        item.description = validated_data.pop('description')
        item.category = validated_data.pop('category')
        item.type = validated_data.pop('type')
        item.unit = validated_data.pop('unit')
        account_no = validated_data.pop('account').get('account_no')
        site_id = DEFAULT_PROJECT_ID
        if item.account:
            site_id = item.account.site.id
        if account_no:
            if item.account:
                account = item.account
                if InventoryAccount.objects.filter(account_no=account_no).exists():
                    account_no = int(account_no) +1
                account.account_no = account_no
                account.save()
            else:
                account = InventoryAccount(name=item.name, account_no=account_no, site_id=site_id)
                account.save()
                item.account = account
        item.save()
        return item


class InventoryAccountSerializer(serializers.ModelSerializer):
    account_category = serializers.CharField(source='get_category', read_only=True)
    site_id = serializers.PrimaryKeyRelatedField(source='site', queryset=Project.objects.all())
    site_name = serializers.ReadOnlyField(source='site.name')

    class Meta:
        model = InventoryAccount
        fields = ('id', 'code', 'name', 'account_no', 'current_balance', 'account_category', 'site_id', 'site_name')


class DemandRowSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(source='item', queryset=Item.objects.all())
    item_name = serializers.ReadOnlyField(source='item.name')

    class Meta:
        model = DemandRow
        fields = ('id', 'purpose', 'item_id', 'item_name', 'quantity', 'unit', 'fulfilled_quantity', 'status')
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }


class DemandDetailsSerializer(serializers.ModelSerializer):
    rows = SerializerMethodField('get_rows', read_only=True)

    class Meta:
        model = Demand
        fields = ('id', 'rows',)

    def get_rows(self, demand):
        rows = demand.rows.all()
        serializer = DemandRowSerializer(instance=rows, many=True)
        return serializer.data


class DemandSerializer(serializers.ModelSerializer):
    site_id = serializers.PrimaryKeyRelatedField(source='site', queryset=Project.objects.all())
    site_name = serializers.ReadOnlyField(source='site.name')
    rows = DemandRowSerializer(many=True)

    class Meta:
        model = Demand
        fields = ('id', 'date', 'purpose', 'site_id', 'site_name', 'rows')
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }

    def create(self, validated_data):
        rows_data = validated_data.pop('rows')
        demand = Demand.objects.create(**validated_data)
        for row_data in rows_data:
            data = dict(row_data)
            row = DemandRow()
            row.item = data.get('item')
            row.unit = data.get('unit','Pieces')
            row.purpose = data.get('purpose','')
            row.status = data.get('status', False)
            row.quantity = data.get('quantity',0.0)
            row.fulfilled_quantity = data.get('fulfilled_quantity',0)
            row.demand = demand
            row.save()
            if row.fulfilled_quantity:
                set_transactions(row, row.demand.date, ['dr', InventoryAccount.objects.get_or_create(
                    site=row.demand.site, name=row.item.name, account_no=row.item.account.account_no)[0],
                                                        row.fulfilled_quantity])
                set_transactions(row, row.demand.date, ['cr', row.item.account, row.fulfilled_quantity])
        return demand

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        demand = Demand.objects.get(pk=instance.id)
        demand.date = validated_data.pop('date',None)
        demand.purpose = validated_data.pop('purpose','')
        demand.site = validated_data.pop('site')
        demand.save()
        for row_data in rows_data:
            data = dict(row_data)
            id = data.get('id', '')
            if id:
                row = DemandRow.objects.get(pk=id)
            else:
                row = DemandRow()

            row.item = data.get('item')
            row.unit = data.get('unit', 'Pieces')
            row.purpose = data.get('purpose', '')
            row.status = data.get('status', False)
            row.quantity = data.get('quantity', 0.0)
            row.fulfilled_quantity = data.get('fulfilled_quantity', 0)
            row.demand = demand
            row.save()
            if row.fulfilled_quantity:
                set_transactions(row, row.demand.date, ['dr', InventoryAccount.objects.get_or_create(
                    site=row.demand.site, name=row.item.name, account_no=row.item.account.account_no)[0],
                                                        row.fulfilled_quantity])
                set_transactions(row, row.demand.date, ['cr', row.item.account, row.fulfilled_quantity])
        return demand


class SiteDemandsSerializer(serializers.ModelSerializer):
    # employee = serializers.StringRelatedField()
    demands = SerializerMethodField('get__site_demands', read_only= True)

    class Meta:
        model = Project
        fields = ('id', 'demands',)

    def get__site_demands(self, site):
        demand_list = site.demands.all()
        serializer = DemandSerializer(instance=demand_list, many=True)
        return serializer.data


class SiteAccountSerializer(serializers.ModelSerializer):
    # employee = serializers.StringRelatedField()
    accounts = SerializerMethodField('get__site_accounts', read_only= True)

    class Meta:
        model = Project
        fields = ('id', 'accounts',)

    def get__site_accounts(self, site):
        acc_list = site.inventory_account.all()
        serializer = InventoryAccountSerializer(instance=acc_list, many=True)
        return serializer.data


class PartySerializer(serializers.ModelSerializer):
    cr_balance = serializers.ReadOnlyField(source='account.current_cr')
    dr_balance = serializers.ReadOnlyField(source='account.current_dr')

    class Meta:
        model = Party


class PurchaseRowSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(source='item', queryset=Item.objects.all())
    item_name = serializers.ReadOnlyField(source='item.name')

    class Meta:
        model = PurchaseRow
        exclude = ['item', 'purchase']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }


class PartyPaymentRowSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartyPayment
        exclude = ['party']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }


class PartyPaymentSerializer(serializers.ModelSerializer):
    rows = PartyPaymentRowSerializer(many=True)
    dr_balance = serializers.ReadOnlyField(source='account.current_dr')
    cr_balance = serializers.ReadOnlyField(source='account.current_cr')

    class Meta:
        model = Party
        fields = ['id', 'name', 'rows', 'dr_balance', 'cr_balance']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
            "name": {
                "read_only": True, "required": False, },
        }

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        party = Party.objects.get(pk=instance.id)
        for row_data in rows_data:
            data = dict(row_data)
            row_id = data.get('id',0)
            if not row_id:
                amount = data.get('amount',0.0)
                date = data.get('date',0.0)
                voucher_no = data.get('voucher_no',1)
                row = PartyPayment(amount=amount, date=date, party=party, voucher_no=voucher_no)
                row.save()
                set_ledger_transactions(row, row.date, ['dr', party.account, row.amount])
                set_ledger_transactions(row, row.date,
                                        ['cr', Account.objects.get_or_create(name="Cash")[0],
                                         row.amount])
        return party


class ConsumptionIARowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumptionRow
        exclude = ['account']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }


class PurchaseInfoSerializer(serializers.ModelSerializer):
    rows = PurchaseRowSerializer(many=True)

    class Meta:
        model = Purchase
        exclude = ['party']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }


class PurchaseSerializer(serializers.ModelSerializer):
    party_id = serializers.PrimaryKeyRelatedField(source='party', queryset=Party.objects.all())
    party_name = serializers.ReadOnlyField(source='party.name')
    pan_no = serializers.ReadOnlyField(source='party.pan_no')
    total_vat = serializers.ReadOnlyField(source='vat')
    total_amt = serializers.ReadOnlyField(source='total')
    rows = PurchaseRowSerializer(many=True)

    class Meta:
        model = Purchase
        exclude = ['party']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }

    def create(self, validated_data):
        rows_data = validated_data.pop('rows')
        purchase = Purchase.objects.create(**validated_data)
        for row_data in rows_data:
            data = dict(row_data)
            row = PurchaseRow()
            row.sn = data.get('sn')
            row.item = data.get('item')
            row.unit = data.get('unit','Pieces')
            row.quantity = data.get('quantity',0.0)
            row.is_vatable = data.get('is_vatable',True)
            row.rate = data.get('rate', 0.0)
            row.discount = data.get('discount',0.0)
            row.purchase = purchase
            row.save()
            iv_account, status = InventoryAccount.objects.get_or_create(
                name=row.item.name, site_id=DEFAULT_PROJECT_ID, account_no=row.item.account.account_no)
            set_transactions(row, row.purchase.date, ['dr', iv_account, row.quantity])
            if not row.is_vatable:
                row_amount = row.quantity*row.rate-row.discount
            else:
                row_amount = row.quantity*row.rate*1.13-row.discount
            set_ledger_transactions(row, row.purchase.date,
                                    ['dr', row.item.ledger,
                                     row_amount])
            if purchase.credit:
                set_ledger_transactions(row, row.purchase.date, ['cr', purchase.party.account,
                                                                 row_amount])
            else:
                set_ledger_transactions(row, row.purchase.date, ['cr', Account.objects.get_or_create(name ='Cash')[0],
                                                                 row_amount])
        return purchase

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        purchase = Purchase.objects.get(pk=instance.id)
        purchase.date = validated_data.pop('date',None)
        purchase.credit = validated_data.pop('credit',False)
        purchase.voucher_no = validated_data.pop('voucher_no')
        purchase.party = validated_data.pop('party')
        purchase.save()
        for row_data in rows_data:
            data = dict(row_data)
            row_id = data.get('id', '')
            if row_id:
                row = PurchaseRow.objects.get(pk=row_id)
                # if not row.item == data.get('item'):
                #     iv_account, status = InventoryAccount.objects.get_or_create(
                #         name=row.item.name, site_id=DEFAULT_PROJECT_ID, account_no=row.item.account.account_no)
                #     set_transactions(row, row.purchase.date, ['cr', iv_account, row.quantity])
                #     set_ledger_transactions(row, row.purchase.date, ['cr', row.item.ledger,
                #                                                      row.quantity*row.rate-row.discount])

            else:
                row = PurchaseRow()
            row.sn = data.get('sn')
            row.item = data.get('item')
            row.unit = data.get('unit','Pieces')
            row.quantity = data.get('quantity',0.0)
            row.is_vatable = data.get('is_vatable',True)
            row.rate = data.get('rate', 0.0)
            row.discount = data.get('discount',0.0)
            row.purchase = purchase
            row.save()
            iv_account, status = InventoryAccount.objects.get_or_create(
                name=row.item.name, site_id=DEFAULT_PROJECT_ID, account_no=row.item.account.account_no)
            set_transactions(row, row.purchase.date, ['dr', iv_account, row.quantity])
            if not row.is_vatable:
                row_amount = row.quantity*row.rate-row.discount
            else:
                row_amount = row.quantity*row.rate*1.13-row.discount
            set_ledger_transactions(row, row.purchase.date,
                                 ['dr', row.item.ledger,
                                  row_amount])
            if purchase.credit:
                set_ledger_transactions(row, row.purchase.date, ['cr', purchase.party.account,
                                                                 row_amount])
            else:
                set_ledger_transactions(row, row.purchase.date, ['cr', Account.objects.get_or_create(name ='Cash')[0],
                                                                 row_amount])

        return purchase


class ConsumptionIASerializer(serializers.ModelSerializer):
    rows = ConsumptionIARowSerializer(many=True)

    class Meta:
        model = InventoryAccount
        exclude = ['site']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
            "name": {
                "read_only": True, "required": False, },
            "code": {
                "read_only": True, "required": False, },
            "account_no": {
                "read_only": True, "required": False, },
            "current_balance": {
                "read_only": True, "required": False, },
        }

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        ia = InventoryAccount.objects.get(pk=instance.id)
        for row_data in rows_data:
            data = dict(row_data)
            id = data.get('id', '')
            if not id:
                row = ConsumptionRow()
                row.sn = data.get('sn')
                row.quantity = data.get('quantity',0.0)
                row.purpose = data.get('purpose',0.0)
                row.date = data.get('date',datetime.date.today)
                row.account = ia
                row.save()
                ia.current_balance -=row.quantity
                ia.save()
        return ia


class PartyPurchaseSerializer(serializers.ModelSerializer):
    purchase = PurchaseInfoSerializer(many=True)
    # create payment rows class
    class Meta:
        model = Party
        fields = ['id', 'purchase','name']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
            "name": {
                "read_only": True, "required": False, },
        }