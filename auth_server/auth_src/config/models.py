from django.db import models


class BaseModel(models.Model):
    """Base model with common fields"""

    created_at = models.DateTimeField(
        verbose_name="생성된 일시",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="수정된 일시",
        auto_now=True,
    )
    deleted_at = models.DateTimeField(
        verbose_name="삭제된 일시",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
