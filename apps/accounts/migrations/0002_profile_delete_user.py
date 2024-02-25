# Generated by Django 4.2 on 2024-02-25 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("is_delete", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "jenis_kelamin",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Laki-Laki", "Laki-Laki"),
                            ("Perempuan", "Perempuan"),
                        ],
                        default=None,
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        help_text="username",
                        max_length=255,
                        unique=True,
                        verbose_name="username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True, max_length=254, verbose_name="email address"
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "db_table": "accounts_user",
            },
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
