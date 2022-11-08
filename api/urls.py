from django.urls import path,include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()  
router.register(r"customers",views.CustomerViewSet)
router.register(r"wallets",views.WalletViewSet)
router.register(r"accounts",views.AccountViewSet)
router.register(r"cards",views.CardViewSet)
router.register(r"transactions",views.TransactionViewSet)
router.register(r"loans",views.LoanViewSet)
router.register(r"receipts",views.ReceiptViewSet)
router.register(r"notifications",views.NotificationsViewSet)


urlpatterns = [
    path("",include(router.urls)),
    path("deposit/", views.AccountDepositView.as_view(), name="deposit-view"),
    path("transfer/", views.AccountTransferView.as_view(), name="transfer-view"),
    path("withdraw/", views.AccountWithdrawView.as_view(), name="withdraw-view"),
    path("requestLoan/", views.AccountRequestLoanView.as_view(), name="loan-rquest-view"),
    path("repay_loan/", views.AccountRepayLoanView.as_view(), name="loan-repay-view"),
    path("buy_airtime/", views.AccountBuyAirtimeView.as_view(), name="airtime-view"),
]
