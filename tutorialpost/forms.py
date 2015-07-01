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
class MyRegistrationForm(UserCreationForm):
  email = forms.EmailField(required =True)
  captcha = CaptchaField()


  class meta:
    model =User
    fields =('username','email', 'password1','password2','captcha')


  def save (self,commit=True):
    user= super(UserCreationForm,self).save(commit=False)
    user.email =self.cleaned_data['email']
    user.captcha =self.cleaned_data['captcha']
    user.set_password(self.cleaned_data['password1'])



    if commit:
      user.save()
