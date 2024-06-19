# Generated by Django 5.0.1 on 2024-02-26 08:25

import django.utils.timezone
import socialmedia.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0009_alter_profiles_cover_photo_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='user_id',
        ),
        migrations.AddField(
            model_name='likes',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='media_url',
            field=models.ImageField(blank=True, null=True, upload_to=socialmedia.models.get_upload_path),
        ),
    ]
