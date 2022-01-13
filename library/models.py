from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image',blank=True)
    bio = models.CharField(max_length=255, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    cover = CloudinaryField('image')
    image_link = models.URLField(max_length=1000, null=False, blank=False, default="https://cloudfront.penguin.co.in/wp-content/uploads/2022/01/9780143454441.jpg")
    subject = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post',null=True)

    def __str__(self):
        return self.author

