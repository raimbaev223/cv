# Generated by Django 3.1.7 on 2021-03-20 07:00

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20210320_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]
