from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('event', views.eventView.as_view(), name="event"),
    path('login', views.loginView.as_view(), name="login"),
    path('register', views.registerView.as_view(), name="register"),
]