# Generated by Django 5.0.7 on 2024-09-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성된 일시"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정된 일시"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, null=True, verbose_name="삭제된 일시"),
                ),
                (
                    "username",
                    models.CharField(max_length=255, unique=True, verbose_name="유저명"),
                ),
                ("password", models.CharField(max_length=255, verbose_name="암호")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="계정 활성화 여부"),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="관리자 권한 여부"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="최고 관리자 권한 여부"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "db_table": "user",
            },
        ),
    ]
