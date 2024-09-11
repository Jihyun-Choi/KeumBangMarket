from django.contrib import admin
from authentication.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin View for User"""

    list_display = (
        "id",
        "username",
        "is_active",
        "is_staff",
        "is_superuser",
    )
