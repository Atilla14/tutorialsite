from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from models import Forum

class ForumForm(forms.ModelForm):
  class Meta:
    model =Forum
    fields = '__all__'

# Create form class for the Registration form
class CaptchaForm(forms.Form):

    email = forms.EmailField(required =True)
    captcha = CaptchaField()

    class meta:
        model =User
        fields =('email','captcha')


