# Generated by Django 5.0.1 on 2024-03-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0014_following_following_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='profile_picture_url',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
