# Generated by Django 2.1 on 2018-08-19 15:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(choices=[('6 months', '6 months'), ('1 YEAR', '1 YEAR'), ('2-5 YEARS', '2-5 YEARS'), ('5-10 YEARS', '5-10 YEARS'), ('10 YEARS OR OLDER', '10 YEARS OR OLDER')], max_length=15)),
                ('breed', models.CharField(max_length=100)),
                ('description', models.TextField(validators=[django.core.validators.MaxLengthValidator(250), django.core.validators.MinLengthValidator(10)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('street_address', models.CharField(max_length=250)),
                ('street_address_2', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=2)),
                ('family_size', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('current_pets_total', models.IntegerField()),
                ('pets_dogs', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, 'This breed requires attention than you can provide at this time.'), django.core.validators.MinValueValidator(0)])),
                ('pets_cats', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('pets_other', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('interest_reason', models.TextField(validators=[django.core.validators.MaxLengthValidator(250), django.core.validators.MinLengthValidator(10)])),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('contact_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxLengthValidator(9999999999)])),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
