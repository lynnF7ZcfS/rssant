# Generated by Django 2.1.7 on 2019-03-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssant_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='dt_updated',
            field=models.DateTimeField(help_text='更新时间'),
        ),
    ]