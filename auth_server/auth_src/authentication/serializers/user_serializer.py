from rest_framework import serializers
from authentication.models.user import User


class UserSerializer(serializers.ModelSerializer):
    """ModelSerializer definition for User Model."""

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, value):
        # 유저명 길이 검사 (3자 이상, 20자 이하)
        if len(value) < 3 or len(value) > 20:
            raise serializers.ValidationError("Username must be between 3 and 20 characters.")
        # 영문자와 숫자로만 구성된 유저명 검사
        if not value.isalnum():
            raise serializers.ValidationError("Username must contain only letters and numbers.")
        return value

    def validate_password(self, value):
        # 비밀번호 길이 검사 (최소 8자 이상)
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters.")
        # 비밀번호에 숫자가 하나 이상 포함되어 있는지 검사
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        # 비밀번호에 대문자가 하나 이상 포함되어 있는지 검사
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        # 비밀번호에 소문자가 하나 이상 포함되어 있는지 검사
        if not any(char.islower() for char in value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        # 비밀번호에 특수 문자가 포함되어 있는지 검사
        if not any(char in "!@#$%^&*()_+-=" for char in value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return value

    def create(self, validated_data):
        # 유저 생성 및 비밀번호 해싱
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user
