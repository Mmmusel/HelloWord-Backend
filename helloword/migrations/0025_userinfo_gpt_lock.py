# Generated by Django 3.2.9 on 2023-05-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloword', '0024_userinfo_cookie_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gpt_lock',
            field=models.CharField(default='', max_length=128, null=True),
        ),
    ]
