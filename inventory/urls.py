from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from inventory import views
from inventory.viewsets import CategoryViewSet, ItemViewSet, InventoryAccountViewSet, SiteDemandsViewSet, DemandsViewSet, \
    PurchaseViewSet, PartyViewSet, SiteInventoryAccountViewSet, InventoryAccountConsumptionViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'site-demands', SiteDemandsViewSet)
router.register(r'demand', DemandsViewSet)
router.register(r'party', PartyViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'account', InventoryAccountViewSet)
router.register(r'site-account', SiteInventoryAccountViewSet)
router.register(r'consumption', InventoryAccountConsumptionViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^next-account-no/$', views.next_account_no, name='next_account'),
                       )