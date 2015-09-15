from rest_framework.response import Response
from employee.models import Employee, EmployeeRole, Salary
from project.permissions import IsOwnerOrReadOnly, IsSiteInchargeOrReadOnly
from user.models import AweUser

__author__ = 'awemulya'


from.models import Project
from .serializer import InChargeSerializer, SitesSerializer, SiteEmployeeSerializer, EmployeeSerializer, RoleSerializer, \
    SalarySerializer, EmployeeSalarySerializer
from rest_framework import viewsets

class InChargeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = AweUser.objects.all()
    serializer = InChargeSerializer(queryset, many=True)

    def perform_create(self, serializer):
            serializer.save()


class SitesViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = SitesSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_admin:
            return Project.objects.all()
        else:
            return self.request.user.project_set.all()

    def perform_create(self, serializer):
            serializer.save()


class RoleViewSet(viewsets.ModelViewSet):

    queryset = EmployeeRole.objects.all()
    serializer_class = RoleSerializer

    def perform_create(self, serializer):
            serializer.save()


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()


class SalaryViewSet(viewsets.ModelViewSet):

    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save()


class SiteEmployeeViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = SiteEmployeeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        # import pdb
        # pdb.set_trace()
        if self.request.user.is_admin:
            return Project.objects.all()
        else:
            # get side id and site obj siteobj.employee.all()
            return self.request.user.project_set.all()

    def perform_create(self, serializer):
            serializer.save()


class EmployeeSalaryViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSalarySerializer

    def perform_create(self, serializer):
            serializer.save()
