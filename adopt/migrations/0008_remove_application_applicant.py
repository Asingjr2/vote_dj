# Generated by Django 2.1 on 2018-08-23 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0007_remove_application_current_pets_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='applicant',
        ),
    ]
