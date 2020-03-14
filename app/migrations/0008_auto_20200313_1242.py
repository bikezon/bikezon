# Generated by Django 3.0.3 on 2020-03-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200313_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followergroup',
            old_name='group_owner',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='followergroup',
            name='group_followers',
        ),
        migrations.AddField(
            model_name='followergroup',
            name='following',
            field=models.ManyToManyField(related_name='following', to='app.UserProfile'),
        ),
    ]
