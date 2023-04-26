# Generated by Django 3.2.9 on 2023-04-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloword', '0022_auto_20230425_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='last_study_date_info',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='readinghistory',
            name='input',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='readinghistory',
            name='output',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='wordscloze',
            name='answers',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wordscloze',
            name='cloze',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='wordsstory',
            name='answers',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wordsstory',
            name='story',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='writinghistory',
            name='input',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='writinghistory',
            name='output',
            field=models.CharField(max_length=4096, null=True),
        ),
    ]