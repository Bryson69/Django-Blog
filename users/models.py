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
    banner = CloudinaryField(default = 'banner_default.jpg', folder = 'blog/banners/' )
    profile_pic = CloudinaryField(default = 'default.jpg', folder = 'blog/profile_pic/' ) 
    
    def __str__(self):
        return f'{self.user.username} Profile'

