from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from inventory.models import Category, Item, InventoryAccount, Demand, DemandRow
from project.models import Project


class CategorySerializer(ModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent.name')

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'parent', 'parent_name')


class ItemSerializer(serializers.ModelSerializer):
    account_no = serializers.ReadOnlyField(source='account.account_no')
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all())
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = ('id', 'code', 'name', 'description', 'category_name', 'type', 'unit', 'account_no', 'category_id')


class InventoryAccountSerializer(serializers.ModelSerializer):
    account_category = serializers.CharField(source='get_category', read_only=True)

    class Meta:
        model = InventoryAccount
        fields = ('id', 'code', 'name', 'account_no', 'opening_balance', 'current_balance', 'account_category')


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
                row.item = data.get('item')
                row.unit = data.get('unit', 'Pieces')
                row.purpose = data.get('purpose', '')
                row.status = data.get('status', False)
                row.quantity = data.get('quantity', 0.0)
                row.fulfilled_quantity = data.get('fulfilled_quantity', 0)
                row.demand = demand
                row.save()
            else:
                row = DemandRow()
                row.item = data.get('item')
                row.unit = data.get('unit','Pieces')
                row.purpose = data.get('purpose','')
                row.status = data.get('status', False)
                row.quantity = data.get('quantity',0.0)
                row.fulfilled_quantity = data.get('fulfilled_quantity',0)
                row.demand = demand
                row.save()

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