from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Organizer)
admin.site.register(RequestEvent)

