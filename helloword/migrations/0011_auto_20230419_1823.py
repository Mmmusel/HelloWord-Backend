# Generated by Django 3.2.9 on 2023-04-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloword', '0010_auto_20230419_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readinghistory',
            name='input',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='wordscloze',
            name='cloze',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='wordsstory',
            name='story',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='writinghistory',
            name='input',
            field=models.CharField(max_length=4096),
        ),
    ]
