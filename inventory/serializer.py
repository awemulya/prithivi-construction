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


class DemandSerializer(serializers.ModelSerializer):
    site_id = serializers.PrimaryKeyRelatedField(source='site', queryset=Project.objects.all())
    site_name = serializers.ReadOnlyField(source='site.name')

    class Meta:
        model = Demand
        fields = ('id', 'date', 'purpose', 'site_id', 'site_name')


class DemandRowSerializer(serializers.ModelSerializer):
    demand_id = serializers.PrimaryKeyRelatedField(source='demand', queryset=Demand.objects.all())
    purpose_name = serializers.ReadOnlyField(source='demand.purpose')

    class Meta:
        model = DemandRow
        fields = ('id', 'site_id', 'site_purpose', 'purpose', 'quantity', 'unit', 'fulfilled_quantity', 'status')


class DemandDetailsSerializer(serializers.ModelSerializer):
    rows = SerializerMethodField('get_rows', read_only=True)

    class Meta:
        model = Demand
        fields = ('id', 'rows',)

    def get_rows(self, demand):
        rows = demand.rows.all()
        serializer = DemandRowSerializer(instance=rows, many=True)
        return serializer.data


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