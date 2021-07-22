from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from .forms import *

# Create your views here.
class eventView(View):
    template_name = "user/event.html"

    def get(self, request):
        return render(request, self.template_name)

class loginView(View):
    template_name = "user/login.html"

    def get(self, request):
        return render(request, self.template_name)

class registerView(View):
    template_name = "user/register.html"

    def get(self, request):
        return render(request, self.template_name)

class organizedEventsView(View):
    template_name = "user/organizedEvents.html"

    def get(self, request):
        return render(request, self.template_name)

class createEventView(View):
    template_name = "user/createEvent.html"

    def get(self, request, user):
        formCreateEvent = CreateEventForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):

        eventName = request.POST.get('eventName')
        eventDescription = request.POST.get('eventDescription')
        eventCategory = request.POST.get('eventCategory')
        eventStart = request.POST.get('eventStart')
        eventEnd = request.POST.get('eventEnd')
        username = User.objects.get(pk=user)

        createEvent = Event(eventName=eventName, eventDescription=eventDescription, eventCategory=eventCategory,
                            eventStart=eventStart, eventEnd=eventEnd, username=username)

        createEvent.save()

        return render(request, self.template_name, {'createEvent': createEvent})

class requestJoinView(View):
    template_name = "user/requestJoin.html"

    def get(self, request):
        return render(request, self.template_name)

class updateEventView(View):
    template_name = "user/updateEvent.html"

    def get(self, request):
        return render(request, self.template_name)

class viewDetailsView(View):
    template_name = "user/viewDetails.html"

    def get(self, request):
        return render(request, self.template_name)

class requestOrganizerView(View):
    template_name = "user/requestOrganizer.html"

    def get(self, request):
        return render(request, self.template_name)

class requestAdminView(View):
    template_name = "user/requestAdmin.html"

    def get(self, request):
        return render(request, self.template_name)        