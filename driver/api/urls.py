from django.urls import path, include
from rest_framework.routers import DefaultRouter
from driver.api.views import DriverViewSet, DeliveryViewSet

router = DefaultRouter()
router.register("drivers", DriverViewSet, basename="driver")
router.register("deliverys", DeliveryViewSet, basename="delivery")

urlpatterns = [
    path('', include(router.urls)),
]
