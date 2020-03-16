from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='resources'), 
    path('getmeetings/', views.getmeetings, name='meetings'), 
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'), 
    path('newmeeting/', views.newMeeting, name='newmeeting'), 
    path('newresource/', views.newResource, name='newresource'), 
    path('loginmessage/', views.loginmessage, name='loginmessage'), 
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'), 
]
