# Generated by Django 3.2.9 on 2023-05-24 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helloword', '0030_auto_20230524_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='has_invite',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='vip_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.CreateModel(
            name='DailyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_time', models.DateField(auto_now_add=True)),
                ('num', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloword.userinfo')),
            ],
        ),
    ]
