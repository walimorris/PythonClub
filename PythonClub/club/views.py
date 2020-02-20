from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource, Event
from django.shortcuts import get_object_or_404
from .forms import MeetingForm, ResourceForm

# Create your views here.
def index(request): 
    return render(request, 'club/index.html')

def getresources(request): 
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html' ,{'resource_list' : resource_list})

def getmeetings(request): 
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html' , {'meeting_list' : meeting_list})

def meetingdetails(request, id): 
    meeting=get_object_or_404(Meeting, pk=id)
    context={
        'meeting' : meeting, 
    }
    return render(request, 'club/meetingdetails.html', context=context)

"""
Form views must account for the Post Data and save this data to the database
"""
def newMeeting(request): 
    form = MeetingForm # which form 
    if request.method == 'Post': 
        form = MeetingForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit = True)
            post.save()  
            form = MeetingForm
    else: 
        form = MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

def newResource(request): 
    form = ResourceForm
    if request.method == 'Post': 
        form = MeetingForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit = True)
            post.save()
            form = ResourceForm
    else: 
        form = ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

