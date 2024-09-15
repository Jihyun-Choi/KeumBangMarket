from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.shortcuts import get_object_or_404

from authentication.serializers import UserDetailSerializer
from config.api_response import api_response
from authentication.models import User


class TokenVerifyAPIView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        token = request.data.get("token")
        if not token:
            return api_response(
                success=False, message="토큰이 제공되지 않았습니다.", status_code=status.HTTP_400_BAD_REQUEST
            )

        try:
            access_token = AccessToken(token)
            if access_token.get("token_type") != "access":
                raise ValidationError("엑세스 토큰만 입력 가능합니다.")
        except (InvalidToken, TokenError):
            # 유효하지 않은 토큰 또는 만료된 토큰일 경우 처리
            return api_response(
                success=False,
                message="유효하지 않은 토큰입니다. 다시 로그인하세요.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            return api_response(success=False, message=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        user_id = access_token.get("user_id")
        user = get_object_or_404(User, id=user_id)
        serializer = UserDetailSerializer(user)

        return api_response(
            success=True, message="토큰 검증 성공하였습니다.", data=serializer.data, status_code=status.HTTP_200_OK
        )
