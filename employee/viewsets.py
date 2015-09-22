from rest_framework import viewsets
from employee.models import SalaryVoucher
from employee.serializer import SalaryVoucherSerializer, SiteSalaryVoucherSerializer
from project.models import Project


class SiteSalaryVoucherViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = SiteSalaryVoucherSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()


class SalaryVoucherViewSet(viewsets.ModelViewSet):

    queryset = SalaryVoucher.objects.all()
    serializer_class = SalaryVoucherSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
