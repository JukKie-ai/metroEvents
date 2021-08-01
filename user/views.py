from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
#class eventView(View):
#    template_name = "user/event.html"
#
#    def get(self, request):
#        eventList = Event.objects.all()
#
#        myFilter = EventFilter(request.GET, queryset=eventList)
#        eventList = myFilter.qs
#
#        context = {'eventList':eventList, 'myFilter':myFilter}
#
#        return render(request, self.template_name, context)

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

    def get(self, request, user):

        if Organizer.objects.filter(username=user).count() != 0:
            account = Organizer.objects.get(username=user)
            obj = Event.objects.all()
        else:
            account = 0
            obj = '0'

        return render(request, self.template_name, {'obj':obj, 'account': account})

def delete(request, id, user):
    event = Event.objects.get(pk=id)
    context = {'user':user, 'event': event}
    event.delete()

    return render(request, 'user/organizedEvents.html', context)
        
class createEventView(View):
    template_name = "user/createEvent.html"

    def get(self, request, user):
        formEvent = EventForm()
        return render(request, self.template_name, {'user': user})

    def post(self, request, user):
        event = EventForm(request.POST)

        eventName = request.POST.get('eventName')
        eventDescription = request.POST.get('eventDescription')
        eventCategory = request.POST.get('eventCategory')
        eventLocation = request.POST.get('eventLocation')
        eventStart = request.POST.get('eventStart')
        eventEnd = request.POST.get('eventEnd')
        organizerID = Organizer.objects.get(username=user)

        createEvent = Event(eventName=eventName, eventDescription=eventDescription, eventCategory=eventCategory,
                                eventLocation=eventLocation, eventStart=eventStart, eventEnd=eventEnd, organizerID=organizerID)

        createEvent.save()

        return render(request, self.template_name, {'createEvent': createEvent})

class requestJoinView(View):
    template_name = "user/requestJoin.html"

    def get(self, request):
        return render(request, self.template_name)

class joinListView(View):
    template_name = "user/joinList.html"

    def get(self, request, user):

        if Organizer.objects.filter(username=user).count() != 0:
            account = Organizer.objects.get(username=user)
            obj = User.objects.all()
            
            if Organizer.objects.filter(username=user).count() != 0:
                account = Organizer.objects.get(username=user)
                obj2 = Event.objects.all() 
            else:
                account = 0
                obj = 0
                obj2 = '0'

        return render(request, self.template_name, {'obj':obj, 'obj2':obj2,'account': account})

    def post(self, request, user):
        status = RequestEvent.objects.get()


def updateEventView(request, id, user):
    event = Event.objects.get(pk=id)
    eventName = request.POST.get('eventName')
    eventDescription = request.POST.get('eventDescription')
    eventCategory = request.POST.get('eventCategory')
    eventLocation = request.POST.get('eventLocation')
    eventStart = request.POST.get('eventStart')
    eventEnd = request.POST.get('eventEnd')
    context = {'user':user, 'event': event}

    username = Organizer.objects.get(username_id=user)

    if request.method == "POST":
        updateEvent = Event(eventID=event.eventID,eventName=eventName, eventDescription=eventDescription, eventCategory=eventCategory,
                                eventLocation=eventLocation, eventStart=eventStart, eventEnd=eventEnd, organizerID=username)

        updateEvent.save()

        return render(request, 'user/updateEvent.html', context)

    return render(request, 'user/updateEvent.html', context)
    
class viewDetailsView(View):
    template_name = "user/viewDetails.html"

    def get(self, request):
        return render(request, self.template_name)

class roleRequestView(View):
    template_name = "user/roleRequest.html"

    def get(self, request):
        return render(request, self.template_name)