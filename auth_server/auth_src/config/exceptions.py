from rest_framework.views import exception_handler
from rest_framework import status
from config.api_response import api_response


def custom_exception_handler(exc, context):
    # 기본 예외 처리
    response = exception_handler(exc, context)

    if response is not None:
        # 401 Unauthorized 처리
        if response.status_code == 401:
            return api_response(
                success=False,
                message="인증되지 않은 유저입니다.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        # 400 Bad Request 처리
        if response.status_code == 400:
            return api_response(
                success=False,
                message="올바르지 않은 데이터입니다.",
                errors=response.data,
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        # 그 외의 일반적인 오류 처리
        return api_response(
            success=False,
            message="예기치 않은 오류가 발생했습니다.",
            errors=response.data,
            status_code=response.status_code,
        )

    # 추가적인 예외 처리
    if isinstance(exc, KeyError):
        return api_response(
            success=False,
            message=f"필수 필드가 누락되었습니다. ({str(exc)})",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    elif isinstance(exc, ValueError):
        return api_response(
            success=False,
            message=f"유효하지 않은 값입니다. ({str(exc)})",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # 기타 예외 처리
    return api_response(
        success=False,
        message="요청을 처리할 수 없습니다. 나중에 다시 시도해 주세요.",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
