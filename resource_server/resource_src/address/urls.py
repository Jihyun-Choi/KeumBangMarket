from django.urls import path
from rest_framework.routers import DefaultRouter
from address.views import AddressViewSet

app_name = "address"
router = DefaultRouter()
router.register(r"", AddressViewSet, basename="address")

urlpatterns = []

urlpatterns += router.urls
