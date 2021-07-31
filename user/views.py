from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib import messages

from .filters import EventFilter

from django.db import connections
from django.db import connection
import MySQLdb


# Create your views here.
class registerView(View):
    template_name = "user/register.html"

    def get(self, request, ):
        return render(request, self.template_name)

    def post(self, request):
        formUser = UserForm(request.POST)
        uname = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if User.objects.filter(pk=uname).count() != 0:
            messages.error(request, "Username already exist!")
        elif confirmPassword != password:
            messages.error(request, "Password doesn't match.")
        else:
            customer = formUser.save(commit=False)
            customer.save()
            return redirect(reverse('user:login'))

        return render(request, self.template_name)

class loginView(View):

    template_name = "user/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if User.objects.filter(pk=uname).count() != 0:
            account = User.objects.get(pk=uname)

            if account.password == pwd:
                return redirect(reverse('user:home', kwargs={'user': uname}))
            else:
                messages.error(request, 'Incorrect Password')
        else:
            messages.error(request, 'Username Does Not Exist')

        return render(request, self.template_name)

class homeView(View):
    template_name = "user/home.html"

    def get(self, request, user):
        return render(request, self.template_name, {'user': user})

class eventView(View):
    template_name = "user/event.html"

    def get(self, request, user):
        eventList = Event.objects.all()

        myFilter = EventFilter(request.GET, queryset=eventList)
        eventList = myFilter.qs

        context = {'user':user, 'eventList':eventList, 'myFilter':myFilter}

        return render(request, self.template_name, context)

def viewDetailsView(request, id, user):
    event = Event.objects.get(pk=id)

    context = {'user':user, 'event':event}
    return render(request, 'user/viewDetails.html', context)

def joinEventView(request, id, user):
    event = Event.objects.get(pk=id)
    username = User.objects.get(pk=user)

    context = {'user':user, 'event':event, 'username':username}

    if request.method == 'POST':
        requestForm = RequestEvent(status=False, username=username, eventID=event)

        requestForm.save()
        return render(request, 'user/joinEvent.html', context)

    return render(request, 'user/joinEvent.html', context)



class organizedEventsView(View):
    template_name = "user/organizedEvents.html"

    def get(self, request):
        return render(request, self.template_name)

class createEventView(View):
    template_name = "user/createEvent.html"

    def get(self, request):
        return render(request, self.template_name)

class requestJoinView(View):
    template_name = "user/requestJoin.html"

    def get(self, request):
        return render(request, self.template_name)

class joinListView(View):
    template_name = "user/joinList.html"

    def get(self, request):
        return render(request, self.template_name)

class updateEventView(View):
    template_name = "user/updateEvent.html"

    def get(self, request):
        return render(request, self.template_name)

class roleRequestView(View):
    template_name = "user/roleRequest.html"
    
    def get(self, request):
        rq = RequestRole.objects.all()
        return render(request, self.template_name,{'rq': rq})
    
    def post(self, request):
        if request.method == "POST":
            rq = RequestRole.objects.all()
            if 'AcceptBtn' in request.POST:
                reqID = request.POST.get("request_id")

                if 'orgReq' in request.POST:
                    organizerReq = 1
                else:
                    organizerReq = 0

                if 'adminReq' in request.POST:
                    administratorReq = 1
                else:
                    administratorReq = 0

                update_request = RequestRole.objects.filter(requestID = reqID).update(setAsOrganizer = organizerReq, setAsAdministrator = administratorReq)
            if 'DenyBtn' in request.POST:
                reqID = request.POST.get("request_id")
                delete_request = RequestRole.objects.filter(requestID = reqID).delete()
                return render(request, self.template_name,{'rq': rq})

        return render(request, self.template_name)
