from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import *

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "eventID",
            "eventName",
            "eventDescription",
            "eventCategory",
            "eventStart",
            "eventEnd",
       ]



