from rest_framework import serializers
from employee.models import SalaryVoucher, SalaryVoucherRow

class SalaryVoucherRowSerializer(serializers.ModelSerializer):
    employee_id = serializers.ReadOnlyField(source='employee.id')
    paid_date = serializers.DateField(format=None)
    start_date = serializers.DateField(format=None)
    last_date = serializers.DateField(format=None)
    
    class Meta:
        model = SalaryVoucherRow
        # exclude = ['employee']
        
class SalaryVoucherSerializer(serializers.ModelSerializer):
    rows = SalaryVoucherRowSerializer(many=True)
    date = serializers.DateField(format=None)

    def create(self, validated_data):
        return SalaryVoucher.objects.create(**validated_data)

    class Meta:
        model = SalaryVoucher
