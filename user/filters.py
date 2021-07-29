from django.db.models import fields
import django_filters

from .models import *

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = [
            'eventName',
            'eventCategory',
        ]