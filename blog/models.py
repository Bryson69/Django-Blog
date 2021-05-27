from django.db import models
from django.db.models.deletion import CASCADE

from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    # image
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=CASCADE)

    # dunder str method
    def __str__(self):
        return self.title

    def __unicode__(self):
        return 

class Category(models.Model):
    categories = models.CharField(max_length=200, null=True)
    def __str__(self):
        return 

    def __unicode__(self):
        return 

