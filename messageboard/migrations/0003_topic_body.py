# Generated by Django 2.1 on 2018-08-20 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0002_auto_20180819_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='body',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(300)]),
        ),
    ]
