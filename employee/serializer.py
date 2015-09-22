from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from employee.models import SalaryVoucherRow, SalaryVoucher, Employee
from project.models import Project
import datetime


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
        sv = SalaryVoucher.objects.create(**validated_data)
        for row_data in rows_data:
            data = dict(row_data)
            row = SalaryVoucherRow()
            row.employee = data.get('employee')
            row.sn = data.get('sn',0)
            row.amount = data.get('amount',0)
            row.paid_date = data.get('paid_date', datetime.datetime.today)
            row.start_date = data.get('start_date', datetime.datetime.today)
            row.last_date = data.get('last_date', datetime.datetime.today)
            row.salary_voucher = sv
            row.save()
        return sv

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('rows')
        sv = SalaryVoucher.objects.get(pk=instance.id)
        sv.date = validated_data.pop('date',datetime.datetime.today)
        sv.voucher_no = validated_data.pop('voucher_no','')
        sv.site = validated_data.pop('site')
        sv.save()
        for row_data in rows_data:
            data = dict(row_data)
            id = data.get('id', '')
            if id:
                row = SalaryVoucherRow.objects.get(pk=id)
                row.employee = data.get('employee')
                row.sn = data.get('sn',1)
                row.amount = data.get('amount',0)
                row.paid_date = data.get('paid_date', datetime.datetime.today)
                row.start_date = data.get('start_date',datetime.datetime.today)
                row.last_date = data.get('last_date', datetime.datetime.today)
                row.salary_voucher = sv
                row.save()
            else:
                row = SalaryVoucherRow()
                row.employee = data.get('employee')
                row.sn = data.get('sn',1)
                row.amount = data.get('amount',0)
                row.paid_date = data.get('paid_date',datetime.datetime.today)
                row.start_date = data.get('start_date',datetime.datetime.today)
                row.last_date = data.get('last_date',datetime.datetime.today)
                row.salary_voucher = sv
                row.save()

        return sv


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