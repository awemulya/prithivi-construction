from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from ledger import views
from ledger.viewsets import AccountViewSet, BankViewSet, BankWithdrawViewSet, VendorViewSet, VendorPaymentViewSet

router = DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'bank', BankViewSet)
router.register(r'bank-withdraw', BankWithdrawViewSet)
router.register(r'vendor', VendorViewSet)
router.register(r'vendor-payment', VendorPaymentViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )