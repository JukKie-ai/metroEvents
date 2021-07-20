from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'