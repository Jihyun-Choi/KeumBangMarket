from django.utils import timezone
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
    """SoftDelete model with is_deleted and deleted_at fields"""

    deleted_at = models.DateTimeField(
        verbose_name="삭제된 일시",
        null=True,
        blank=True,
    )
    is_deleted = models.BooleanField(
        verbose_name="삭제 여부",
        default=False,
    )

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """Soft delete: is_deleted를 True로 설정하고, deleted_at에 삭제 시간 기록"""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


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
    is_deleted = models.BooleanField(
        verbose_name="삭제 여부",
        default=False,
    )

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """Soft delete: is_deleted를 True로 설정하고, deleted_at에 삭제 시간 기록"""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
