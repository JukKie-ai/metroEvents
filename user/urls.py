from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('event', views.eventView.as_view(), name="event"),
    path('login', views.loginView.as_view(), name="login"),
    path('register', views.registerView.as_view(), name="register"),
    path('organizedEvents', views.organizedEventsView.as_view(), name="organizedEvents"),
    path('createEvent', views.createEventView.as_view(), name="createEvent"),
    path('requestJoin', views.requestJoinView.as_view(), name="requestJoin"),
    path('joinList', views.joinListView.as_view(), name="joinList"),
    path('updateEvent', views.updateEventView.as_view(), name="updateEvent"),
    path('viewDetails', views.viewDetailsView.as_view(), name="viewDetails"),
    path('roleRequest',views.roleRequestView.as_view(), name="roleRequest"),
]