from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image',blank=True,default="https://image.cnbcfm.com/api/v1/image/105897632-1557241558937avatar-e1541360922907.jpg?v=1557241670&w=1600&h=900")
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
    
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50, blank=True)
    author = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    image_link = models.URLField(max_length=1000, null=False, blank=False, default="https://cloudfront.penguin.co.in/wp-content/uploads/2022/01/9780143454441.jpg")
    subject = models.CharField(max_length=50, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post',null=True)

    def __str__(self):
        return self.author

    @classmethod
    def search_by_title(cls, search_term):
        return  cls.objects.filter(title__icontains=search_term)
        
