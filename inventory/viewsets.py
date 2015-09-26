from rest_framework import viewsets
from inventory.models import Category, Item, InventoryAccount, Demand, Purchase, Party
from inventory.serializer import CategorySerializer, ItemSerializer, InventoryAccountSerializer, SiteDemandsSerializer, \
    DemandSerializer, PurchaseSerializer, PartySerializer, SiteAccountSerializer, ConsumptionIASerializer
from project.models import Project
from project.permissions import IsAdminOrReadOnly


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

class SiteInventoryAccountViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = SiteAccountSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()


class DemandsViewSet(viewsets.ModelViewSet):

    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class PartyViewSet(viewsets.ModelViewSet):

    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()


class PurchaseViewSet(viewsets.ModelViewSet):

    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class InventoryAccountConsumptionViewSet(viewsets.ModelViewSet):

    queryset = InventoryAccount.objects.all()
    serializer_class = ConsumptionIASerializer
    # permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()