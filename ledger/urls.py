from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from ledger.viewsets import AccountViewSet

router = DefaultRouter()
router.register(r'account', AccountViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )