from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from config.api_response import api_response
from address.models import Address
from address.serializers.address_serializer import AddressSerializer


class AddressViewSet(
    mixins.CreateModelMixin,  # POST
    mixins.ListModelMixin,  # GET (List)
    mixins.DestroyModelMixin,  # DELETE
    viewsets.GenericViewSet,
):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_user_from_token(self, token):
        # TODO: gRPC 통신 부분을 나중에 구현하고, 해당 함수를 서비스 또는 유틸리티로 분리
        # 현재는 임시로 user_id 1을 반환
        return 1  # 임시 user_id

    def get_queryset(self):
        # 로그인한 사용자의 삭제되지 않은 주소만 조회
        return Address.objects.filter(user=self.request.user, is_deleted=False)

    @swagger_auto_schema(
        operation_summary="주소 목록 조회",
        operation_description="로그인한 사용자의 주소 목록을 조회합니다. 삭제되지 않은 주소만 반환됩니다.",
        responses={200: AddressSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="주소 생성",
        operation_description="새로운 주소를 생성합니다. 로그인한 사용자의 주소만 생성 가능합니다.",
        request_body=AddressSerializer,
        responses={201: AddressSerializer()},
    )
    def perform_create(self, serializer):
        # 주소 생성 시 유저 정보를 자동으로 추가
        token = self.request.headers.get("Authorization").split(" ")[1]
        user_id = self.get_user_from_token(token)  # gRPC로 인증된 user_id를 가져옴
        serializer.context["user_id"] = user_id  # user_id를 context로 전달
        serializer.save()

    @swagger_auto_schema(
        operation_summary="주소 삭제",
        operation_description="특정 주소를 삭제합니다. 실제로 데이터를 삭제하지 않고, 소프트 삭제를 수행합니다.",
        responses={
            204: openapi.Response(description="주소가 성공적으로 삭제되었습니다."),
            404: openapi.Response(description="해당 주소를 찾을 수 없습니다."),
            500: openapi.Response(description="주소 삭제 중 오류가 발생했습니다."),
        },
    )
    def destroy(self, request, *args, **kwargs):
        try:
            address = self.get_object()
            address.delete()  # SoftDeleteModel에서 정의된 delete 메서드 사용
            return api_response(
                success=True, message="주소가 성공적으로 삭제되었습니다.", status_code=status.HTTP_204_NO_CONTENT
            )
        except Address.DoesNotExist:
            return api_response(
                success=False, message="해당 주소를 찾을 수 없습니다.", status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return api_response(
                success=False,
                message="주소 삭제 중 오류가 발생했습니다.",
                errors=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
