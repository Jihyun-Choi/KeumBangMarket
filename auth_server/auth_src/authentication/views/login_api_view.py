from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from config.api_response import api_response


class LoginAPIView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data

        return api_response(
            success=True,
            message="User logged in successfully.",
            data=response_data,
            status_code=status.HTTP_200_OK,
        )
