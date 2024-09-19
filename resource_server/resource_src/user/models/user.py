from django.db import models
from config.models import TimeStampedModel


class User(TimeStampedModel):
    """User model that extends from BaseModel"""

    username = models.CharField(
        verbose_name="유저명",
        max_length=255,
        unique=True,
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

    class Meta:
        """Meta definition for User."""

        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"

    def __str__(self):
        return self.username
