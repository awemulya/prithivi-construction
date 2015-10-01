from rest_framework import serializers
from ledger.models import Account, Bank, BankWithdrawAndDeposit, Vendor, VendorPayments, Transaction
from ledger.models import Account, set_transactions as set_ledger_transactions


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account


class BankSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='account.code')
    current_dr = serializers.FloatField(source='account.current_dr')
    current_cr = serializers.FloatField(source='account.current_cr')

    class Meta:
        model = Bank
        exclude = ['account']

    def create(self, validated_data):
        account = validated_data.pop('account')
        code = account.get('code')
        current_dr = account.get('current_dr')
        current_cr = account.get('current_cr')
        # site_id = validated_data.pop('site').get('id')
        bank = Bank.objects.create(**validated_data)

        if bank.account:
            account = bank.account
            account.code = code
            account.current_dr = current_dr
            account.current_cr = current_cr
            account.save()
        else:
            account = Account(name=bank.name, code=code, current_dr=current_dr, current_cr=current_cr)
            account.save()
            bank.account = account
        bank.save()
        return bank

    def update(self, instance, validated_data):
        bank = Bank.objects.get(pk=instance.id)
        bank.name = validated_data.pop('name')
        bank.address = validated_data.pop('address')
        bank.phone_no = validated_data.pop('phone_no')
        bank.save()
        account = validated_data.pop('account')
        code = account.get('code')
        current_dr = account.get('current_dr')
        current_cr = account.get('current_cr')

        if bank.account:
            account = bank.account
            account.code = code
            account.name = bank.name
            account.current_dr = current_dr
            account.current_cr = current_cr
            account.save()
        else:
            account = Account(name=bank.name, code=code, current_dr=current_dr, current_cr=current_cr)
            account.save()
            bank.account = account
            bank.save()
        return bank


class BankWithdrawRowSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankWithdrawAndDeposit
        exclude = ['bank']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }


class TransactionSerializer(serializers.ModelSerializer):

    date = serializers.ReadOnlyField(source='journal_entry.date')
    voucher_no = serializers.ReadOnlyField(source='journal_entry.source.voucher_no')

    class Meta:
        model = Transaction
        exclude = ['account','journal_entry']
        # extra_kwargs = {
        #     "id": {
        #         "read_only": False, "required": False, },
        # }


class AccountTransactionSerializer(serializers.ModelSerializer):

    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Account


class BankWSOrDepoSerializer(serializers.ModelSerializer):
    rows = BankWithdrawRowSerializer(many=True)
    dr_balance = serializers.ReadOnlyField(source='account.current_dr')
    cr_balance = serializers.ReadOnlyField(source='account.current_cr')

    class Meta:
        model = Bank
        fields = ['id', 'name', 'rows', 'dr_balance', 'cr_balance']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
            "name": {
                "read_only": True, "required": False, },
        }

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        bank = Bank.objects.get(pk=instance.id)
        for row_data in rows_data:
            data = dict(row_data)
            row_id = data.get('id',0)
            if not row_id:
                amount = data.get('amount',0.0)
                date = data.get('date',0.0)
                voucher_no = data.get('voucher_no',1)
                is_deposit = data.get('is_deposit',False)
                row = BankWithdrawAndDeposit(amount=amount, date=date, bank=bank, voucher_no=voucher_no,
                                             is_deposit=is_deposit)
                row.save()
                if bank.account:
                    if row.is_deposit:
                        set_ledger_transactions(row, row.date, ['cr',Account.objects.get_or_create(name='Cash')[0], row.amount])
                        set_ledger_transactions(row, row.date, ['dr', bank.account, row.amount])
                    else:
                        set_ledger_transactions(row, row.date, ['cr', bank.account, row.amount])
                        set_ledger_transactions(row, row.date, ['dr', Account.objects.get_or_create(name='Cash')[0], row.amount])

        return bank


class VendorSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='account.code')
    current_dr = serializers.FloatField(source='account.current_dr')
    current_cr = serializers.FloatField(source='account.current_cr')

    class Meta:
        model = Bank
        exclude = ['account']

    def create(self, validated_data):
        account = validated_data.pop('account')
        code = account.get('code')
        current_dr = account.get('current_dr')
        current_cr = account.get('current_cr')
        # site_id = validated_data.pop('site').get('id')
        vendor = Vendor.objects.create(**validated_data)

        if vendor.account:
            account = vendor.account
            account.code = code
            account.current_dr = current_dr
            account.current_cr = current_cr
            account.save()
        else:
            account = Account(name=vendor.name, code=code, current_dr=current_dr, current_cr=current_cr)
            account.save()
            vendor.account = account
        vendor.save()
        return vendor

    def update(self, instance, validated_data):
        vendor = Vendor.objects.get(pk=instance.id)
        vendor.name = validated_data.pop('name')
        vendor.address = validated_data.pop('address')
        vendor.phone_no = validated_data.pop('phone_no')
        vendor.save()
        account = validated_data.pop('account')
        code = account.get('code')
        current_dr = account.get('current_dr')
        current_cr = account.get('current_cr')

        if vendor.account:
            account = vendor.account
            account.name = vendor.name
            account.code = code
            account.current_dr = current_dr
            account.current_cr = current_cr
            account.save()
        else:
            account = Account(name=vendor.name, code=code, current_dr=current_dr, current_cr=current_cr)
            account.save()
            vendor.account = account
        vendor.save()
        return vendor


class VendorPaymentsRowSerializer(serializers.ModelSerializer):
    bank_id = serializers.PrimaryKeyRelatedField(source='bank',queryset=Bank.objects.all())
    bank_name = serializers.ReadOnlyField(source='bank.name')
    class Meta:
        model = VendorPayments
        exclude = ['vendor','bank']
        extra_kwargs = {
        "id": {
        "read_only": False, "required": False, },
        }


class VendorPaymentsSerializer(serializers.ModelSerializer):
    rows = VendorPaymentsRowSerializer(many=True)
    dr_balance = serializers.ReadOnlyField(source='account.current_dr')
    cr_balance = serializers.ReadOnlyField(source='account.current_cr')

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'rows', 'dr_balance', 'cr_balance']
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
            "name": {
                "read_only": True, "required": False, },
        }

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        vendor = Vendor.objects.get(pk=instance.id)
        for row_data in rows_data:
            data = dict(row_data)
            row_id = data.get('id',0)
            if not row_id:
                amount = data.get('amount',0.0)
                date = data.get('date',0.0)
                voucher_no = data.get('voucher_no',1)
                bank = data.get('bank')
                row = VendorPayments(amount=amount, date=date, vendor=vendor, voucher_no=voucher_no, bank=bank)
                row.save()
                if vendor.account:
                    set_ledger_transactions(row, row.date, ['cr', vendor.account, row.amount])
                    set_ledger_transactions(row, row.date, ['dr', row.bank.account, row.amount])

        return vendor
