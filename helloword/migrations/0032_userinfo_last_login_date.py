# Generated by Django 3.2.9 on 2023-05-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloword', '0031_auto_20230524_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='last_login_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]