from rest_framework import status
from rest_framework.generics import CreateAPIView

from authentication.serializers import UserSerializer
from config.api_response import api_response


class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            success=True,
            message="User created successfully.",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED,
        )
