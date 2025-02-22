from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, StateViewSet

router = DefaultRouter()
router.register(r'states', StateViewSet)  # API for states
router.register(r'properties', PropertyViewSet)  # API for properties

urlpatterns = [
    path('', include(router.urls)),
]
