from django.urls import path
from rest_framework.routers import DefaultRouter
from authentication.views import LogoutAPIView, LoginAPIView, RegisterAPIView
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "authentication"
router = DefaultRouter()

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
