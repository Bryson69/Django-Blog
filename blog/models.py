from django.db import models
from django.db.models.deletion import CASCADE

from cloudinary.models import CloudinaryField
from django.db.models.fields.related import ManyToManyField

from django.db.models.signals import pre_save
from django_blog.utils import unique_slug_generator
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BookmarkManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() .filter()

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=255, null=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, default=1)
    
    archive = models.ForeignKey('Archive', null=True, on_delete=models.PROTECT, default=1)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    content = models.TextField()
    image = CloudinaryField(default = 'default.jpg')
    image_caption = models.CharField(max_length = 100, default = 'Photo by Blog')
    
    date_posted = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')


    author = models.ForeignKey(User, on_delete=CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    objects = models.Manager()  # default manager
    bookmarkmanager = BookmarkManager()  # custom manager
    # dunder str method
    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = CloudinaryField(default = 'default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return


class Archive(models.Model):
    name = models.CharField(max_length=400, null=True)
    image = CloudinaryField(default = 'default.jpg')
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return


class Comment(models.Model):
    name = models.CharField(max_length=255, default=None )
    post = models.ForeignKey(Post, on_delete=models.CASCADE,default=None, related_name='comments')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return 

