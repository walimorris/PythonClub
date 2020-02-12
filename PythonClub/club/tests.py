from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource, Event
from .views import index, getresources, getmeetings, meetingdetails
from django.urls import reverse
from django.contrib.auth.models import User

# Test Models 
class MeetingTest(TestCase): 
    def setup(self): 
        meeting = Meeting(meetingtitle='Python Contest', meetinglocation='Seattle Central College Library', 
        meetingagenda = 'A contest for all students! To develop a new website for the college', 
        meetingdate='2020-02-12')
        return meeting
    
    def test_string(self): 
        meet = self.setup()
        self.assertEqual(str(meet), meet.meetingtitle)

    def test_table(self): 
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase): 
    def setup(self): 
        resource = Resource(resourcename='Python Practice', resourcetype='website', 
        resourcedescription = 'Python algorithm and data structure practice')
        return resource

    def test_string(self): 
        resource = self.setup()
        self.assertEqual(str(resource), resource.resourcename)

    def test_table(self): 
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase): 
    def setup(self): 
        event = Event(eventtitle='Pizza Party', eventlocation='Central Seattle College Dining Hall', 
        eventdescription='A fun and exciting pizza party with Python Club members', 
        eventdate='2020-02-12')
        return event

    def test_string(self): 
        event = self.setup()
        self.assertEqual(str(event), event.eventtitle)

    def test_table(self): 
        self.assertEqual(str(Event._meta.db_table), 'event')

# Test Views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self): 
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetResourcestest(TestCase): 
    def test_view_url_accessible_by_name(self): 
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

class GetMeetingTest(TestCase): 
    def test_view_url_accessible_by_name(self): 
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

    def setUp(self): 
        self.meetingid = Meeting.objects.create(meetingtitle='Memberships', meetingdate='2020-02-12', meetingtime='19:30:10', 
        meetinglocation='Juanita Drive Starbucks', meetingagenda='Discussion regarding memberships')
    
    def test_meeting_detail_success(self): 
        """Test to ensure the primary key(meeting id) is passed to the meeting 
        detail and handled correctly. seyUp() is an example of a sample meeting
        object. meetingid is the id created for the meeting object. meetingdetail 
        is responsible for creating a url link from Python Club's homepage menu, as 
        clickable, to a more descriptive post of that clicked meeting taking place. 
        To handle this responsibilty, this method ensures the id for a meeting is 
        passable.
        """ 
        response = self.client.get(reverse('meetingdetails', args=(self.meetingid.id, ))) # trailing comma required for single-item tuples
        self.assertEqual(response.status_code, 200)

        
    



