from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from .forms import *

# Create your views here.
class dashboardView(View):
    template_name = "user/dashboard.html"

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
