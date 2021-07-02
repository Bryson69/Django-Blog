from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.db.models.deletion import CASCADE

from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    banner = models.ImageField(upload_to='banners',blank=True)
    # profile_pic = ImageField(default = 'default.jpg', folder = 'blog/profile_pic/' ) 
    # banner = ImageField(default = 'banner_default.jpg', folder = 'blog/banners/' )
    # models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'

