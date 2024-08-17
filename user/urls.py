from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    SuccessRegisterView,
    LogoutView,
    UserBalanceCreateView,
    UserBalanceAddView,
    UserBalanceListView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path(
        "success-register/",
        SuccessRegisterView.as_view(),
        name="success-register"
        ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('userbalance/create/', UserBalanceCreateView.as_view(), name='user-balance-create'),
    path('userbalance/update/<int:pk>/', UserBalanceAddView.as_view(), name='user-balance-update'),
    path('userbalance/', UserBalanceListView.as_view(), name='user-balance-list'),
]
