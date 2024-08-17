from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, LoginViewSet, UserBalanceViewSet

router = DefaultRouter()
router.register("register", RegisterViewSet, basename="register")
router.register("login", LoginViewSet, basename="login")
router.register("userbalance", UserBalanceViewSet, basename="userbalance")
urlpatterns = [
    path("", include(router.urls)),
]
