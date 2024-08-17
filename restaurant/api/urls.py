from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.api.views import RestaurantViewSet, MenuItemViewSet

router = DefaultRouter()
router.register("restaurants", RestaurantViewSet, basename="restaurant")
router.register("menuitems", MenuItemViewSet, basename="menuitem")

urlpatterns = [
    path("", include(router.urls)),
]
