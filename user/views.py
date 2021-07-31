from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from .forms import *

from django.db import connections
from django.db import connection
import MySQLdb


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

class viewDetailsView(View):
    template_name = "user/viewDetails.html"

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