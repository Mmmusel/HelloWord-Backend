# Generated by Django 4.2 on 2023-04-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("username", models.CharField(max_length=64, unique=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("password_hash", models.CharField(max_length=64, unique=True)),
                ("daily_words_count", models.IntegerField(default=200, null=True)),
            ],
        ),
    ]
