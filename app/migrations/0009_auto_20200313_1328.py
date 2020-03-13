# Generated by Django 3.0.3 on 2020-03-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200313_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='app.UserProfile'),
        ),
        migrations.DeleteModel(
            name='FollowerGroup',
        ),
    ]
