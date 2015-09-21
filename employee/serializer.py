from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from employee.models import SalaryVoucherRow, SalaryVoucher
from project.models import Project


class SalaryVoucherRowSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(source='employee', queryset=Employee.objects.all())
    employee_name = serializers.ReadOnlyField(source='employee.name')

    class Meta:
        model = SalaryVoucherRow
        fields = ('id', 'sn', 'employee_id', 'employee_name', 'paid_date', 'amount', 'start_date', 'last_date')
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }


class SalaryVoucherSerializer(serializers.ModelSerializer):
    site_id = serializers.PrimaryKeyRelatedField(source='site', queryset=Project.objects.all())
    site_name = serializers.ReadOnlyField(source='site.name')
    rows = SalaryVoucherRowSerializer(many=True)

    class Meta:
        model = SalaryVoucher
        fields = ('id', 'date', 'voucher_no', 'site_id', 'site_name', 'rows')
        extra_kwargs = {
            "id": {
                "read_only": False, "required": False, },
        }

    def create(self, validated_data):
        rows_data = validated_data.pop('rows')
        demand = SalaryVoucher.objects.create(**validated_data)
        for row_data in rows_data:
            data = dict(row_data)
            row = SalaryVoucherRow()
            row.item = data.get('item')
            row.unit = data.get('unit','Pieces')
            row.purpose = data.get('purpose','')
            row.status = data.get('status', False)
            row.quantity = data.get('quantity',0.0)
            row.fulfilled_quantity = data.get('fulfilled_quantity',0)
            row.demand = demand
            row.save()
        return demand

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        demand = SalaryVoucher.objects.get(pk=instance.id)
        demand.date = validated_data.pop('date',None)
        demand.purpose = validated_data.pop('purpose','')
        demand.site = validated_data.pop('site')
        demand.save()
        for row_data in rows_data:
            data = dict(row_data)
            id = data.get('id', '')
            if id:
                row = SalaryVoucherRow.objects.get(pk=id)
                row.item = data.get('item')
                row.unit = data.get('unit', 'Pieces')
                row.purpose = data.get('purpose', '')
                row.status = data.get('status', False)
                row.quantity = data.get('quantity', 0.0)
                row.fulfilled_quantity = data.get('fulfilled_quantity', 0)
                row.demand = demand
                row.save()
            else:
                row = SalaryVoucherRow()
                row.item = data.get('item')
                row.unit = data.get('unit','Pieces')
                row.purpose = data.get('purpose','')
                row.status = data.get('status', False)
                row.quantity = data.get('quantity',0.0)
                row.fulfilled_quantity = data.get('fulfilled_quantity',0)
                row.demand = demand
                row.save()

        return demand


class SiteSalaryVoucherSerializer(serializers.ModelSerializer):
    # employee = serializers.StringRelatedField()
    payrolls = SerializerMethodField('get__site_sv', read_only= True)

    class Meta:
        model = Project
        fields = ('id', 'payrolls',)

    def get__site_sv(self, site):
        voucher_list = site.salary_voucher.all()
        serializer = SalaryVoucherSerializer(instance=voucher_list, many=True)
        return serializer.data