from django.db import models
import os

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(null=True)

class Profiles(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    bio = models.TextField()
    profile_picture_url = models.ImageField(null=True,blank=True,upload_to="images/")
    cover_photo_url = models.ImageField(null=True,blank=True,upload_to="images/")
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_followers = models.IntegerField(default=0)
    no_of_following = models.IntegerField(default=0)
    no_of_posts = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Check if profile_picture_url has changed
        if self._state.adding or self.profile_picture_url != self.__class__.objects.get(pk=self.pk).profile_picture_url:
            # Extract relative path from profile_picture_url
            relative_path = self.profile_picture_url.name
            # Concatenate "images/" prefix with relative path
            image_url = "images/" + relative_path
            # Update profile_picture_url in related Posts
            Posts.objects.filter(user_id=self.user_id).update(profile_picture_url=image_url)
        super().save(*args, **kwargs)
class Following(models.Model):
    user_name = models.CharField(max_length=255)
    following_id = models.IntegerField(default=0)
    following = models.CharField(max_length=255)

def get_upload_path(instance, filename):
    """
    Determine the upload path based on the media type.
    """
    if instance.media_type == 'Image':
        return os.path.join('images/', filename)
    elif instance.media_type == 'Video':
        return os.path.join('videos/', filename)
    else:
        return os.path.join('others/', filename)
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    post_title = models.TextField(max_length=255)
    profile_picture_url = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    media_type = models.CharField(max_length=10)
    media_url = models.ImageField(null=True,blank=True,upload_to=get_upload_path)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    shares_count = models.IntegerField(default=0)
    downloads_count = models.IntegerField(default=0)
    report_count = models.IntegerField(default=0)

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    # user_id = models.IntegerField()
    username = models.CharField(max_length=250,null=False)
    report_date = models.DateTimeField(auto_now_add=True)
class Likes(models.Model):
    like_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    # user_id = models.IntegerField()
    username = models.CharField(max_length=250,null=False)
    like_date = models.DateTimeField(auto_now_add=True)

class Messages(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    group_id = models.IntegerField(null=True)
    message_content = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Grouptbl(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class SearchHistory(models.Model):
    search_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    search_query = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    # user_id = models.IntegerField()
    username = models.CharField(max_length=250,null=False)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

class Notifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    source_id = models.IntegerField()
    notification_type = models.CharField(max_length=20)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)