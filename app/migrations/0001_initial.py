# Generated by Django 3.0.3 on 2020-03-07 13:44

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='media/product_images/')),
                ('dateAdded', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('views', models.IntegerField(default=0)),
                ('available', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='media/profile_images')),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('stars', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
            ],
            options={
                'verbose_name_plural': 'SubCategories',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(1.0)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('item', models.PositiveSmallIntegerField()),
                ('product', models.ManyToManyField(to='app.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ManyToManyField(to='app.SubCategory'),
        ),
    ]
