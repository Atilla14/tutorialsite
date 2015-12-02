from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from tutorialpost.models import Forum, Opencv
from django.http import HttpResponse ,HttpResponseRedirect
from forms import  CaptchaForm
from forms import ForumForm as ArticleForm
# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)


    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):

  return render_to_response('registration/loggedin.html',{'full_name':request.user.username})

def invalid_login(request):

  return render_to_response('invalid_login.html')

def logout(request):

  return render_to_response('registration/logout.html')


def home (request):
    return render (request, "home.html")

@login_required
def getforum (request):

    return render_to_response('article.html',
                              {'articles' :Forum.objects.all() })
@login_required
def getforumfromid(request,article_id=1):
    return render_to_response('articleind.html',
                              {'article':Forum.objects.get(id = article_id)})


# this one is for the user registration form functions


def register_user(request):

  if request.method == 'POST':
    form = MyRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/register_success')
    else:

        args = {}
        args.update(csrf(request))
        args['form'] =form
        return render(request,'register.html',args)
  args = {}
  args.update(csrf(request))
  args['form'] =MyRegistrationForm()
  return render_to_response('register.html',args)


def register_success(request):
  return render_to_response ('register_successful.html')


def create(request):

  if request.POST:
    form=ArticleForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/forum/all')

  else:
    form=ArticleForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response("create_forum.html",args)


def getopencv(request):
    return render_to_response("opencv.html",{'Opencv':Opencv.objects.all().order_by("-date")},)
