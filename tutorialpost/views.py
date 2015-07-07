from django.contrib.auth import login
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from tutorialpost.models import Forum
from django.http import HttpResponse ,HttpResponseRedirect
from forms import  CaptchaForm
from forms import ForumForm as ArticleForm
# Create your views here.


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


def articles (request):

    return render_to_response('article.html',
                              {'articles' :Forum.objects.all() })

def article(request,article_id=1):
    return render_to_response('articleind.html',
                              {'article':Forum.objects.get(id = article_id)})


# this one is for the user registration form functions


def register_user(request):
    if not request.POST:
        return render(request,'register.html', {'user_creation_form' :UserCreationForm(),'captcha_form':CaptchaForm()})


    elif request.POST:

        user_creation_form = UserCreationForm(request.POST)
        captch_form = CaptchaForm(request.POST)
        if user_creation_form.is_valid():
            if captch_form.is_valid():

                new_user = user_creation_form.save()
                new_user.email =captch_form.cleaned_data['email']
                new_user.save()

            # log user in
                return redirect('/register_success/')

        # else if both forms are not valid
        return render(request,'register.html', {'user_creation_form' :user_creation_form,'captcha_form':captch_form})


def register_success(request):
  return render_to_response ('register_successful.html')



def opencvcook(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    return render_to_response('opencv.html',
                              {'articles':Opencv.objects.all(),
                               'language':language})

def Opencv(request,article_id =1):
    return render_to_response('article.html',{'Opencv' : Opencv.objects.get(id = article_id)})

def language (request,language = 'en-gb'):
    response = HttpResponse("Setting language to %s" % language)

    response.set_cookie('lang',language)
    request.session['lang'] =language

    return response
     

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