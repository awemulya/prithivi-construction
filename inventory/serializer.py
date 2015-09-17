from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from inventory.models import Category, Item


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
        model = Item
        fields = ('id', 'code', 'name', 'account_no', 'opening_balance', 'current_balance', 'account_category')