# Generated by Django 3.1.7 on 2021-03-20 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20210320_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='bg_image',
        ),
        migrations.RemoveField(
            model_name='home',
            name='subtitle1',
        ),
        migrations.RemoveField(
            model_name='home',
            name='subtitle2',
        ),
        migrations.RemoveField(
            model_name='home',
            name='subtitle3',
        ),
    ]