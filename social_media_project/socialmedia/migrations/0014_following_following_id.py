# Generated by Django 5.0.1 on 2024-02-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0013_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='following_id',
            field=models.IntegerField(default=0),
        ),
    ]
