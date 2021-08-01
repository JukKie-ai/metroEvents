from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('event', views.eventView.as_view(), name="event"),
    path('login', views.loginView.as_view(), name="login"),
    path('register', views.registerView.as_view(), name="register"),
    path('<user>/organizedEvents', views.organizedEventsView.as_view(), name="organizedEvents"),
    path('<user>/createEvent', views.createEventView.as_view(), name="createEvent"),
    path('<user>/delete/<id>', views.delete, name="delete"),
    path('requestJoin', views.requestJoinView.as_view(), name="requestJoin"),
    path('<user>/joinList', views.joinListView.as_view(), name="joinList"),
    path('<user>/updateEvent/<id>', views.updateEventView, name="updateEvent"),
    path('viewDetails', views.viewDetailsView.as_view(), name="viewDetails"),
    path('roleRequest',views.roleRequestView.as_view(), name="roleRequest"),
]