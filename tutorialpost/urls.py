from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from tutorialpost.models import Post
from tutorialpost.models import Opencv
from tutorialpost.models import AVR
from tutorialpost.models import Forum

urlpatterns = patterns('',                       
                       url(r'^$',ListView.as_view(
                           queryset=(Opencv.objects.all().order_by("-date"),AVR.objects.all().order_by("-date")),
                           template_name ="home.html")),
                       url(r'^latest/$',ListView.as_view(
                           queryset=Post.objects.all().order_by("-date")[:2],
                           template_name ="latest.html")),

                       url(r'^latest/2$',ListView.as_view(
                           queryset=Post.objects.all().order_by("-date")[2:10],
                           template_name ="latest.html")),


                       url(r'^opencv/$','tutorialpost.views.getopencv'),

                       url(r'^opencv/2$',ListView.as_view(
                           queryset=Opencv.objects.all().order_by("-date")[5:10],
                           template_name ="opencv.html")),

                       url(r'^avr/$',ListView.as_view(
                           queryset=AVR.objects.all().order_by("-date")[:5],
                           template_name ="avr.html")),
                       
                       url(r'^avr/$',ListView.as_view(
                           queryset=AVR.objects.all().order_by("-date")[:5],
                           template_name ="avr.html")),
                       url(r'^avr/2$',ListView.as_view(
                           queryset=AVR.objects.all().order_by("-date")[5:10],
                           template_name ="avr.html")),

                       url(r'^(?P<pk>\d+)$',DetailView.as_view(
                           model = Post,
                           template_name = "individual.html")),

                       url(r'^all/$',ListView.as_view(queryset=Forum.objects.all().order_by("-id")[:5],
                           template_name ="article.html")),
                       
                       url(r'^get/(?P<article_id>\d+)/$', 'tutorialpost.views.getforumfromid'),


                       )
