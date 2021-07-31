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
        