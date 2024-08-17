from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.api.views import HomePageViewSet

router = DefaultRouter()
router.register('', HomePageViewSet, basename='home')

urlpatterns = [
    path('', include(router.urls)),
]
