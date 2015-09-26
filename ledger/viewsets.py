from rest_framework import viewsets
from ledger.models import Account
from ledger.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()