from django.test import TestCase
from django.test import Client
from .models import Meeting, MeetingMinute, Resource, Event
from .views import index, getresources, getmeetings, meetingdetails
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import * 

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

# Login and Logout tests
class New_Product_authentication_test(TestCase): 
    def setUp(self): 
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'P@assw0rd1')
        self.type = Resource.objects.create(resourcetype= 'website')
        self.prod = Resource.objects.create(resourcename = 'resource1', producttype = self.type)

    def test_redirect_if_not_logged_in(self): 
        response = self.client.get(reverse('newresource'))
        self.assertRedirects(response, 'accounts/login/?next=/club/newresource/')
    
    def test_Logged_in_uses_correct_template(self): 
        login = self.client.login(username = 'testuser1', password = 'P@assw0rd1')
        response = self.client.get(reverse('newresource1'))
        self.assertEqual(str(response.status.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/newresource.html')

# Forms test
class MeetingFormTest(TestCase): 
    def setUp(self): 
        self.meetingform = MeetingForm.objects.create(meetingtitle='welcome', meetingdate='2000-12-31', 
        meetinglocation='Starbucks', meetingAgenda='Welcome the newest members')

    def test_MeetingForm_valid(self): 
        form = MeetingForm(data={'meetingtitle':'welcome', 'meetingdate':'2000-12-31', 
        'meetinglocation':'Starbucks', 'meetingAgenda':'Welcome the newest members'})
        self.assertTrue(form.is_valid())
    
    def test_MeetingForm_invalid(self): 
        form = MeetingForm(data={'meetingtitle':"", 'meetingdate':'20001231', 
        'meetinglocation':"", 'meetingAgenda':""})
        self.assertFalse(form.is_valid())
        