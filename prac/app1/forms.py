from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import UserProfile
class customform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' ,'password2']


class settingform(forms.ModelForm):
    class Meta:
        model = User
        exclude =('password','is_staff','is_active','date_joined','last_login',"is_superuser",'user_permissions','groups')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude =('user','pic','valid_seller','company_name')

class picForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=['pic']