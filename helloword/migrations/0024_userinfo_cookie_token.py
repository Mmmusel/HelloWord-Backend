# Generated by Django 3.2.9 on 2023-05-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloword', '0023_auto_20230426_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='cookie_token',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
