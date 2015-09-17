from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from inventory.models import Category, Item


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'parent', 'children')


CategorySerializer.base_fields['parent'] = CategorySerializer()
CategorySerializer.base_fields['children'] = CategorySerializer(many=True)


class ItemSerializer(serializers.ModelSerializer):
    account_no = serializers.ReadOnlyField(source='account.account_no')
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all())

    class Meta:
        model = Item
        fields = ('id', 'code', 'name', 'description', 'category', 'type', 'unit', 'account_no')


class InventoryAccountSerializer(serializers.ModelSerializer):
    account_category = serializers.CharField(source='get_category', read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'code', 'name', 'account_no', 'opening_balance', 'current_balance', 'account_category')