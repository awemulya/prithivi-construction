from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from inventory.viewsets import CategoryViewSet, ItemViewSet, InventoryAccountViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'account', InventoryAccountViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )