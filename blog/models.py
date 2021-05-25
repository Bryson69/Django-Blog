from django.db import models
from django.db.models.deletion import CASCADE

from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    CATEGORIES_CHOICES = (
        ('lifestyle', 'lifestyle'),
        ('travel', 'travel'),
        ('fashion', 'fashion'),
    )
    title = models.CharField(max_length=200, null=True)
    content = models.TextField()
    # category
    # image
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=CASCADE)

    # dunder str method
    def __str__(self):
        return self.title

    def __unicode__(self):
        return 

class Categories(models.Model):
    title = models.CharField(max_length=200, null=True)
    lifestyle = models.CharField(max_length=150, null=True)
    travel = models.CharField(max_length = 150, null=True)
    fashion = models.CharField(max_length = 150, null=True)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

