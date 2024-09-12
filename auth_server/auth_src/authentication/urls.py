from django.urls import path
from rest_framework.routers import DefaultRouter


app_name = "authentication"
router = DefaultRouter()

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
]

urlpatterns += router.urls
