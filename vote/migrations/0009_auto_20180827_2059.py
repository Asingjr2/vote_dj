# Generated by Django 2.1 on 2018-08-28 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0008_delete_volunteerjob'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recommendation',
            options={'verbose_name': 'message'},
        ),
    ]