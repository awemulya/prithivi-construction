from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from employee.models import Employee, EmployeeRole
from project.models import Project
from user.models import AweUser

__author__ = 'awemulya'


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'address', 'start_date',)
        depth = 1
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


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
                  'date_joined', 'site_id', 'role_id', 'employee_age')


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
        el = site.employee.all()
        serializer = EmployeeSerializer(instance=el, many=True)
        return serializer.data
