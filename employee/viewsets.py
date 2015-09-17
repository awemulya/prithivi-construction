from rest_framework.response import Response
from rest_framework import viewsets
from employee.models import SalaryVoucher, SalaryVoucherRow
from employee.serializer import SalaryVoucherSerializer, SalaryVoucherRowSerializer

class SalaryVoucherRowViewSet(viewsets.ModelViewSet):
	serializer_class = SalaryVoucherRowSerializer
	queryset = SalaryVoucherRow.objects.all()
