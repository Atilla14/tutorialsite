from django.db import models
import urlparse
from django import template
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Opencv(models.Model):
    title =models.CharField(max_length=140)
    url =EmbedVideoField()
    description =models.TextField()
    date =models.DateTimeField()

    def __unicode__(self):
        return self.title


class Forum(models.Model):

    title =models.CharField(max_length=140)
    description =models.TextField()
    date =models.DateTimeField()

    def __unicode__(self):
        return self.title



class AVR(models.Model):
    
    title =models.CharField(max_length=140)
    url =EmbedVideoField()
    description =models.TextField()
    date =models.DateTimeField()

    def __unicode__(self):
        return self.title    

    
class Post(models.Model):
    title = models.CharField(max_length = 140)
    url =models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateTimeField()
    def __unicode__(self):
        return self.title



