# Generated by Django 2.1 on 2018-08-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0002_auto_20180819_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
