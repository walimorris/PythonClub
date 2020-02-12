from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='resources'), 
    path('getmeetings/', views.getmeetings, name='meetings'), 
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'), 
]
