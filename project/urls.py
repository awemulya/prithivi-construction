from django.conf.urls import patterns, url, include
from project import views
from rest_framework.routers import DefaultRouter
from project.viewsets import SitesViewSet, SiteEmployeeViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'sites', SitesViewSet)
router.register(r'employee',EmployeeViewSet)
router.register(r'site-employee',SiteEmployeeViewSet)
urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^app/$', views.dashboard, name='dashboard'),
                       url(r'^employees/$', views.employee_list, name='employee_list'),
                       )