# Generated by Django 3.2.9 on 2023-05-16 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helloword', '0026_emailresettoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfo',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='helloword.userinfo'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='userstudylist',
            name='create_type',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='wordlist',
            name='create_type',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.CreateModel(
            name='PublicListCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('check_time', models.DateTimeField(auto_now=True)),
                ('check_status', models.CharField(default='', max_length=128, null=True)),
                ('public_list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloword.wordlist')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helloword.userinfo')),
                ('user_study_list_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helloword.userstudylist')),
            ],
        ),
    ]