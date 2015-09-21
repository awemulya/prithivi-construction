from rest_framework import viewsets
from rest_framework.response import Response

from inventory.models import Category, Item, InventoryAccount, Demand
from inventory.serializer import CategorySerializer, ItemSerializer, InventoryAccountSerializer, SiteDemandsSerializer, \
    DemandSerializer
from project.models import Project


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


class SiteDemandsViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = SiteDemandsSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()


class DemandsViewSet(viewsets.ModelViewSet):

    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        import pdb
        pdb.set_trace()
        serializer.save()

    def perform_update(self, serializer):
        import pdb
        pdb.set_trace()
        serializer.save()