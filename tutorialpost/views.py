from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from tutorialpost.models import Forum
from django.http import HttpResponse ,HttpResponseRedirect
from forms import MyRegistrationForm
from forms import ForumForm as ArticleForm
from PIL import Image,ImageDraw,ImageFilter,ImageFont

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('/templates/error/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('/templates/error/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
  username =request.POST.get('username','')
  password = request.POST.get('password','')
  user =auth.authenticate(username=username,password=password)

  if user is not None:
    auth.login(request,user)
    return HttpResponseRedirect('/accounts/loggedin')
  else:
    return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):

  return render_to_response('loggedin.html',{'full_name':request.user.username})

def invalid_login(request):

  return render_to_response('invalid_login.html')

def logout(request):

  return render_to_response('logout.html')


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
  if request.method == 'POST':
    form = MyRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/accounts/register_success')

  args = {}
  args.update(csrf(request))

  args['form'] =MyRegistrationForm()

  return render_to_response('register.html',args)


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