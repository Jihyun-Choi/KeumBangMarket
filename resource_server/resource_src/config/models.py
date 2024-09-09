from django.db import models


class BaseModel(models.Model):
    """Base model with created_at fields"""

    created_at = models.DateTimeField(
        verbose_name="생성된 일시",
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    """SoftDelete model with deleted_at fields"""

    deleted_at = models.DateTimeField(
        verbose_name="삭제된 일시",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class TimeStampedModel(BaseModel):
    """TimeStampe model with updated_at and deleted_at fields"""

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
