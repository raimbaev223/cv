# Generated by Django 3.1.7 on 2021-03-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20210320_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualities',
            name='first',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='qualities',
            name='fourth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='qualities',
            name='second',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='qualities',
            name='third',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skilllevel',
            name='frameworks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skilllevel',
            name='html_css',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skilllevel',
            name='python',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skilllevel',
            name='web_design',
            field=models.IntegerField(),
        ),
    ]
