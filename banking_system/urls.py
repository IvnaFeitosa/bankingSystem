from django.urls import path
from .views import CustomerCreateView, AccountCreateView, DepositView, WithdrawalView, BalanceView

urlpatterns = [
    path('register/', CustomerCreateView.as_view(), name='create_customer'),
    path('account/', AccountCreateView.as_view(), name='create_account'),
    path('deposit/<int:account_id>/', DepositView.as_view(), name= 'deposit'),
    path('withdrawal/<int:account_id>/', WithdrawalView.as_view(), name='Withdrawal'),
    path('balance/<int:account_id>/', BalanceView.as_view(), name='balance'),
    
]