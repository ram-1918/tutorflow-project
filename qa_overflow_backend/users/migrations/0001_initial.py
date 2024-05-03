# Generated by Django 5.0.4 on 2024-05-03 18:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("firstname", models.CharField(blank=True, max_length=25)),
                ("lastname", models.CharField(blank=True, max_length=25)),
                ("email", models.EmailField(blank=True, max_length=55, unique=True)),
                ("password", models.CharField(blank=True, max_length=16)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Admin", "admin"),
                            ("Regular", "regular"),
                            ("Anon", "anon"),
                        ],
                        default="anon",
                        max_length=10,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Users",
            },
        ),
    ]
