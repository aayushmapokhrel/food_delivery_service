from django.urls import path
from .views import TransactionCreateView, TransactionListView

urlpatterns = [
    path('create/', TransactionCreateView.as_view(), name='create_transaction'),
    path('list/', TransactionListView.as_view(), name='transaction_list'),
]
