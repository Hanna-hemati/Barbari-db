# Generated by Django 4.2.8 on 2023-12-30 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cargo",
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
                ("driver_name", models.CharField(max_length=200)),
                ("quantity", models.IntegerField()),
                ("losses", models.IntegerField()),
                (
                    "cargo_type",
                    models.CharField(
                        choices=[
                            ("turkey", "بوقلمون"),
                            ("hen", "مرغ"),
                            ("checken", "جوجه"),
                            ("egg", "تخم مرغ"),
                        ],
                        default="turkey",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PoultryFarmers",
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
                ("phone_number", models.IntegerField()),
                ("city", models.CharField(max_length=100)),
                (
                    "cargo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="barbari.cargo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
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
                ("name", models.CharField(max_length=200)),
                ("license_plate_number", models.CharField(max_length=500)),
                ("capacity", models.IntegerField()),
                (
                    "cargo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="barbari.cargo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChickenCo",
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
                ("phone_number", models.IntegerField()),
                ("city", models.CharField(max_length=100)),
                (
                    "cargo_type",
                    models.CharField(
                        choices=[
                            ("turkey", "بوقلمون"),
                            ("hen", "مرغ"),
                            ("checken", "جوجه"),
                            ("egg", "تخم مرغ"),
                        ],
                        default="turkey",
                        max_length=10,
                    ),
                ),
                (
                    "cargo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="barbari.cargo",
                    ),
                ),
            ],
        ),
    ]
