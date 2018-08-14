from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, auto_created=True, default=1)
    title = models.CharField(max_length=128)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    uploaded_media = models.FileField(verbose_name='Image or Video', default="mediafiles/Ubuntu.jpg")
    image_caption = models.TextField(verbose_name="Image or Video caption")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="News Post"
        verbose_name_plural = "News Posts"


class CustomerReview(models.Model):
    name = models.CharField(max_length=64, verbose_name= "Name", blank=True, null=True) 
    email = models.EmailField(verbose_name="Email")
    user_contribution = models.TextField() 
    
    def __str__(self):
        return self.name
