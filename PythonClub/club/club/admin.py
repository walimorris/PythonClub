from django.contrib import admin
from .models import Meeting, MeetingMinute, Resource, Event

admin.site.register(Meeting)
admin.site.register(MeetingMinute)
admin.site.register(Resource)
admin.site.register(Event)
