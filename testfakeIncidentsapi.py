from django.test import TestCase,Client
from monitor.models import Incident
from fakemonitorservice.models import FakeIncident

class TestFakeIncidentsApi(TestCase):
    def setUp(self):
        pass

    def test_incident_is_available_in_api(self):
        c = Client()
        FakeIncident.objects.create( incident = "sample incident" )
        response = c.get('/fake/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()),1)
        print(response.json())
        self.assertEqual(response.json()[0]['fields']['incident'], "sample incident")
