from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from employee.viewsets import SiteSalaryVoucherViewSet, SalaryVoucherViewSet

router = DefaultRouter()
router.register(r'site-payrolls', SiteSalaryVoucherViewSet)
router.register(r'payroll', SalaryVoucherViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )