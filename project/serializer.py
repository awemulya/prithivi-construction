import datetime
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from employee.models import Employee, EmployeeRole, Salary, Payment
from project.models import Project
from user.models import AweUser
from user.serializer import  UserIDSerializer

__author__ = 'awemulya'


class SitesSerializer(serializers.ModelSerializer):
    incharge = UserIDSerializer(many=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'address', 'start_date', 'incharge')
        depth = 1
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }
    def create(self, validated_data):
        rows_data = validated_data.pop('incharge')
        site = Project.objects.create(**validated_data)
        for row_data in rows_data:
            data = dict(row_data)
            user = AweUser.objects.get(pk=data.get('id'))
            site.incharge.add(user)
        return site

    def update(self, instance, validated_data):
        rows_data = validated_data.pop('incharge')
        site = Project.objects.get(pk=instance.id)
        site.name = validated_data.pop('name')
        site.description = validated_data.pop('description')
        site.address = validated_data.pop('address')
        site.start_date = validated_data.pop('start_date')
        site.incharge.clear()
        site.save()
        for row_data in rows_data:
            data = dict(row_data)
            id = data.get('id', '')
            if id:
                user = AweUser.objects.get(pk=data.get('id'))
                site.incharge.add(user)
        return site

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeRole
        fields = ('id', 'role', 'description')
        depth = 1


class EmployeeSerializer(serializers.ModelSerializer):
    site_id = serializers.PrimaryKeyRelatedField(source='site', queryset=Project.objects.all())
    role_id = serializers.PrimaryKeyRelatedField(source='role', queryset=EmployeeRole.objects.all())
    role_name = serializers.PrimaryKeyRelatedField(source='role.role', read_only=True)
    employee_age = serializers.IntegerField(source='age', read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'address', 'date_of_birth', 'role_name', 'sex','marital_status',
                  'date_joined', 'site_id', 'role_id', 'employee_age', 'status', 'phone')


class SalarySerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(source='employee', queryset=Employee.objects.all())

    class Meta:
        model = Salary
        fields = ('id', 'salary', 'date', 'employee_id')


class PaymentSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(source='employee', queryset=Employee.objects.all())
    monthly_salary = serializers.IntegerField(source='current_salary', read_only=True)
    salary_amount = serializers.IntegerField(source='amount', read_only=True)

    class Meta:
        model = Payment
        fields = ('id', 'absent_days', 'date', 'year', 'monthly_salary', 'salary_amount', 'month', 'employee_id')


class InChargeSerializer(serializers.ModelSerializer):
    sites = SerializerMethodField('get_sites', read_only= True)

    class Meta:
        model = AweUser
        fields = ('id', 'name')
        depth = 2

    def get_sites(self):
        # from django.db.models import Q
        sites = self.incharge_set.all()
        serializer = SitesSerializer(instance=sites, many=True)
        return serializer.data


class SiteEmployeeSerializer(serializers.ModelSerializer):
    # employee = serializers.StringRelatedField()
    employee = SerializerMethodField('get_employees', read_only= True)

    class Meta:
        model = Project
        fields = ('id', 'employee',)

    def get_employees(self, site):
        employee_list = site.employee.all()
        serializer = EmployeeSerializer(instance=employee_list, many=True)
        return serializer.data


class EmployeeSalarySerializer(serializers.ModelSerializer):
    # employee = serializers.StringRelatedField()
    employee_salaries = SerializerMethodField('get_salaries', read_only= True)

    class Meta:
        model = Employee
        fields = ('id', 'employee_salaries',)

    def get_salaries(self, employee):
        salary_list = employee.salary.all()
        serializer = SalarySerializer(instance=salary_list, many=True)
        return serializer.data


class EmployeePaymentSerializer(serializers.ModelSerializer):
    # employee = serializers.StringRelatedField()
    employee_payments = SerializerMethodField('get_payments', read_only= True)

    class Meta:
        model = Employee
        fields = ('id', 'employee_payments',)

    def get_payments(self, employee):
        salary_list = employee.payment.all()
        serializer = PaymentSerializer(instance=salary_list, many=True)
        return serializer.data