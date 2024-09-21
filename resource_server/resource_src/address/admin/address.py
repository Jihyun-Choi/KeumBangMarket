from django.contrib import admin
from address.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Admin View for Address"""

    list_display = (
        "id",
        "user",
        "address_line",
        "postal_code",
        "created_at",
        "deleted_at",
        "is_deleted",
    )
    search_fields = (
        "user__username",
        "address_line",
        "postal_code",
    )
    list_filter = ("deleted_at",)
    ordering = ("-created_at",)
