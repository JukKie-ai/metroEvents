from django.db import models

EVENT_CHOICES = [('Seminars', 'Seminars'), ('Conferences', 'Conferences'), ('Trade Shows', 'Trade Shows'), ('Workshops', 'Workshops'),]

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Administrator(models.Model):
    adminID = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=50)
    eventDescription = models.TextField()
    eventCategory = models.CharField(choices=EVENT_CHOICES, max_length=100)
    eventLocation = models.CharField(max_length=100)
    eventStart = models.DateField()
    eventEnd = models.DateField()

class RequestRole(models.Model):
    requestID = models.AutoField(primary_key=True)
    setAsOrganizer = models.BooleanField(default=False)
    setAsAdministrator = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class RequestEvent(models.Model):
    requestEventID = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)