from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model for authentication

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

#Chatgpt


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    # Add additional fields as needed

class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)


class VideoCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class TutorialVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    # Add additional fields as needed, e.g., likes, comments, etc.



class Feedback(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    video = models.ForeignKey(TutorialVideo, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class CommunityMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
from django.db import models
from django.contrib.auth.models import User

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completion_date = models.DateField()
    # Add fields for certificate details like name, completion text, etc.

