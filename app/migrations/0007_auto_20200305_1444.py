# Generated by Django 3.0.3 on 2020-03-05 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200305_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='id',
            new_name='profile_id',
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile'),
        ),
    ]
