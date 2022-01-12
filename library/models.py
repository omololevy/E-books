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

class SubscriptionRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    your_address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    age = models.CharField(max_length=30)

