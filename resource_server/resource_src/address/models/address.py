from django.db import models
from config.models import SoftDeleteModel


class Address(SoftDeleteModel):
    """Address model for managing user shipping addresses"""

    user = models.ForeignKey(
        "user.User",
        verbose_name="유저",
        on_delete=models.CASCADE,
        related_name="user_addresses",
    )
    address_line = models.CharField(
        verbose_name="주소",
        max_length=255,
    )
    postal_code = models.CharField(
        verbose_name="우편번호",
        max_length=20,
    )

    class Meta:
        """Meta definition for Address."""

        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        db_table = "addresses"

    def __str__(self):
        return f"{self.user.username}: {self.postal_code}"
