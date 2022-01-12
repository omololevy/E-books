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
    cover = CloudinaryField('image',blank=True)
    subject = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.author

