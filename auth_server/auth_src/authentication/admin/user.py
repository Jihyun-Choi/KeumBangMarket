from django.contrib import admin
from authentication.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin View for User"""

    list_display = (
        "id",
        "username",
        "created_at",
        "updated_at",
        "deleted_at",
        "is_active",
        "is_staff",
        "is_superuser",
    )
