# Generated by Django 3.0.3 on 2020-03-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200309_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]