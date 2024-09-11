from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from config.models import BaseModel


class UserManager(BaseUserManager):
    """User manager to handle user creation"""

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    """User model that extends from BaseModel"""

    username = models.CharField(
        verbose_name="유저명",
        max_length=255,
        unique=True,
    )
    password = models.CharField(
        verbose_name="암호",
        max_length=255,
    )
    is_active = models.BooleanField(
        verbose_name="계정 활성화 여부",
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name="관리자 권한 여부",
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name="최고 관리자 권한 여부",
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta definition for User."""

        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"

    def __str__(self):
        return self.username
