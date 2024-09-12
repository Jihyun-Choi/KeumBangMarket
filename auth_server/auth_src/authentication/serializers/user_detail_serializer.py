from authentication.models.user import User
from authentication.serializers import UserSerializer


class UserDetailSerializer(UserSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "created_at",
            "updated_at",
            "deleted_at",
            "is_active",
            "is_staff",
        ]
