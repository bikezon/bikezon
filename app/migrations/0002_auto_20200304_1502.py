# Generated by Django 3.0.4 on 2020-03-04 15:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='stars',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(1.0)]),
        ),
    ]
