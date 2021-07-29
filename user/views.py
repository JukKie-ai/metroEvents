from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib import messages

from .filters import EventFilter

# Create your views here.
class eventView(View):
    template_name = "user/event.html"

    def get(self, request):
        eventList = Event.objects.all()

        myFilter = EventFilter(request.GET, queryset=eventList)
        eventList = myFilter.qs

        context = {'eventList':eventList, 'myFilter':myFilter}

        return render(request, self.template_name, context)

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


class loginView(View):

    template_name = "user/login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name)

    def post(self, request):
        form = LoginForm(request.POST)
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if User.objects.filter(pk=uname).count() != 0:
            account = User.objects.get(pk=uname)

            if account.password == pwd:
                return redirect(reverse('user:Home', kwargs={'user': uname}))
            else:
                messages.error(request, 'Incorrect Password')
        else:
            messages.error(request, 'Username Does Not Exist')

        return render(request, self.template_name)

class registerView(View):
    template_name = "user/register.html"

    def get(self, request):
        formUser = UserForm()
        return render(request, self.template_name)

    def post(self, request):
        formUser = UserForm(request.POST)
        uname = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        #if len(uname) < 4 and len(password) < 8:
            #messages.error(request, "Username and Password are too short.")
        #if User.objects.filter(pk=uname).count() != 0 and len(password) < 8:
            #messages.error(
            #request, "Username already exist and Password is too short.")
        #elif len(uname) < 4:
            #messages.error(request, "Username is too short.")
        if User.objects.filter(pk=uname).count() != 0:
            messages.error(request, "Username already exist!")
        #elif len(password) < 8:
            #messages.error(request, "Password is too short.")
        elif confirmPassword != password:
            messages.error(request, "Password doesn't match.")
        else:
            customer = formUser.save(commit=False)
            customer.save()
            return redirect(reverse('user:login'))

        return render(request, self.template_name)

class roleRequestView(View):
    template_name = "user/roleRequest.html"

    def get(self, request):
        return render(request, self.template_name)
