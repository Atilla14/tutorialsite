from django.contrib.contenttypes.models import ContentType
from django import forms
from django.db import models
import urlparse
from django import template
from django.db import models
from embed_video.fields import EmbedVideoField
CORE_APP_LABEL = 'core'


# Create your models here.
class TutorialModel(models.Model):
    topic = models.TextField(max_length=140,help_text= "Title of the topic you wish to contribute to")
    tutor = models.TextField(max_length= 100,help_text= "Your name as you wish to be seen as the author of the tutorials")

    id = models.CharField
    def __unicode__(self):
        return self.title

class TopicsModel(models.Model):
    topic= models.ForeignKey(TutorialModel,help_text= "select the topic under which this tutorial is classified")
    title =models.CharField(max_length=140)
    url =EmbedVideoField()
    description =models.TextField()
    date =models.DateTimeField()
    id = models.CharField

    def __unicode__(self):
        return self.title


class Forum(models.Model):

    title =models.CharField(max_length=140)
    description =models.TextField()
    date =models.DateTimeField()
    guys = forms.ModelChoiceField(queryset=ContentType)

    def __unicode__(self):
        return self.title



class AVR(models.Model):
    title =models.CharField(max_length=140)
    url =EmbedVideoField()
    description =models.TextField()
    date =models.DateTimeField()
    id = models.CharField
    def __unicode__(self):
        return self.title

class Opencv(models.Model):
    title =models.CharField(max_length=140)
    url =EmbedVideoField()
    description =models.TextField()
    date =models.DateTimeField()
    id = models.CharField
    def __unicode__(self):
        return self.title
    
class Post(models.Model):
    title =models.CharField(max_length=140)
    description =models.TextField()
    date =models.DateTimeField()
    id = models.CharField
    url =models.CharField(max_length=500)
    def __unicode__(self):
        return self.title




