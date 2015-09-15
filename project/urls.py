from django.conf.urls import patterns, url, include
from project import views
from rest_framework.routers import DefaultRouter
from project.viewsets import SitesViewSet, SiteEmployeeViewSet, EmployeeViewSet, RoleViewSet, EmployeeSalaryViewSet, \
    SalaryViewSet, EmployeePaymentsViewSet

router = DefaultRouter()
router.register(r'sites', SitesViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'salary', SalaryViewSet)
router.register(r'role', RoleViewSet)
router.register(r'site-employee', SiteEmployeeViewSet)
router.register(r'employee-salary', EmployeeSalaryViewSet)
router.register(r'employee-payments', EmployeePaymentsViewSet)
urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^app/$', views.dashboard, name='dashboard'),
                       url(r'^employees/$', views.employee_list, name='employee_list'),
                       )