from django.db import models
from django.db.models.deletion import CASCADE

from cloudinary.models import CloudinaryField

from django.db.models.signals import pre_save
from django_blog.utils import unique_slug_generator

from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=255, null=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    content = models.TextField()
    image = CloudinaryField(default = 'default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(User, on_delete=CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)

    # dunder str method
    def __str__(self):
        return self.title

    def __unicode__(self):
        return 

def slug_generator(sender, instance, *args, **kwargs ):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return 

