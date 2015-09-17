from rest_framework import viewsets
from rest_framework.response import Response

from inventory.models import Category, Item, InventoryAccount
from inventory.serializer import CategorySerializer, ItemSerializer, InventoryAccountSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
            serializer.save()


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()


class InventoryAccountViewSet(viewsets.ModelViewSet):

    queryset = InventoryAccount.objects.all()
    serializer_class = InventoryAccountSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()