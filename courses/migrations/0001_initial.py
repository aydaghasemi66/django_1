# Generated by Django 4.2.3 on 2023-08-10 08:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Trainer",
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
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(default="defualt.png", upload_to="trainer"),
                ),
                ("twitter", models.CharField(default="#", max_length=255)),
                ("facebook", models.CharField(default="#", max_length=255)),
                ("instagram", models.CharField(default="#", max_length=255)),
                ("linkdin", models.CharField(default="#", max_length=255)),
                ("status", models.BooleanField(default=False)),
                ("updated_datetime", models.DateTimeField(auto_now=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("skills", models.ManyToManyField(to="courses.skills")),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                    "image",
                    models.ImageField(default="defualt2.jpg", upload_to="course"),
                ),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("counted_views", models.IntegerField(default=0)),
                ("counted_like", models.IntegerField(default=0)),
                ("available_seat", models.IntegerField(default=0)),
                (
                    "schedule",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 8, 10, 1, 53, 54, 575564)
                    ),
                ),
                ("status", models.BooleanField(default=False)),
                ("price", models.IntegerField(default=0)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("category", models.ManyToManyField(to="courses.category")),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.trainer",
                    ),
                ),
            ],
            options={"ordering": ("-created_date",),},
        ),
    ]
