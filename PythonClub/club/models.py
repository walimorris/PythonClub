from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model): 
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.CharField(max_length=255)

    def __str__(self): 
        return self.meetingtitle

    class Meta: 
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinute(models.Model): 
    meetingminuteId=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingminuteattendance=models.ManyToManyField(User)
    meetingminutetext=models.TextField()

    def __str__(self): 
        return self.meetingId

    class Meta: 
        db_table='meetingminute'
        verbose_name_plural='meetingminutes'

class Resource(models.Model): 
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255) 
    resourceurl=models.URLField(null=True, blank=True)
    resourceentrydate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.CharField(max_length=255)


    def __str__(self): 
        return self.resourcename

    class Meta: 
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model): 
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)


    def __str__(self): 
        return self.eventtitle

    class Meta: 
        db_table='event'
        verbose_name_plural='events'