from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class roleForm(forms.ModelForm):
    class Meta:
        model = RequestRole
        fields = '__all__'
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "firstName",
            "lastName"
        ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
