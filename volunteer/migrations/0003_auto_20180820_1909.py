# Generated by Django 2.1 on 2018-08-20 23:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_auto_20180820_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerapplication',
            name='contact_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
