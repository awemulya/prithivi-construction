from rest_framework import viewsets
from ledger.models import Account, Bank, Vendor
from ledger.serializers import AccountSerializer, BankWSOrDepoSerializer, BankSerializer, VendorPaymentsSerializer, \
    VendorSerializer
from ledger.models import Account
from project.permissions import IsAdminOrReadOnly


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class BankViewSet(viewsets.ModelViewSet):

    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class BankWithdrawViewSet(viewsets.ModelViewSet):

    queryset = Bank.objects.all()
    serializer_class = BankWSOrDepoSerializer
    # permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class VendorPaymentViewSet(viewsets.ModelViewSet):

    queryset = Vendor.objects.all()
    serializer_class = VendorPaymentsSerializer
    # permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()

    def perform_update(self, serializer):
        serializer.save()

# class BankWithdrawViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or my Videos.
#     """
#
#     def list(self, request):
#         bank_id = request.query_params.get('Id')
#         bank_amount = request.query_params.get('amount')
#         bank_date = request.query_params.get('date')
#         pk = int(bank_id)
#         amount = float(bank_amount)
#         date_time = datetime.strptime(bank_date, "%Y-%m-%d")
#         date = date_time.date()
#         bank = Bank.objects.get(pk=pk)
#         if bank.account:
#             set_ledger_transactions(bank, date, ['dr', Account.objects.get_or_create(name="Cash")[0], amount])
#             set_ledger_transactions(bank, date, ['cr', bank.account, amount])
#         serializer = BankSerializer(bank, context={'request': request})
#         return Response(serializer.data)


class VendorViewSet(viewsets.ModelViewSet):

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()