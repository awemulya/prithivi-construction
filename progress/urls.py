from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from progress.viewsets import SiteProgressViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'site-tasks', SiteProgressViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )