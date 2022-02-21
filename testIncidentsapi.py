from django.test import TestCase,Client
from monitor.models import Incident

class TestIncidentsApi(TestCase):
    def setUp(self):
        pass

    def test_incident_is_available_in_api(self):
        c = Client()
        Incident.objects.create( incident = "sample incident" )
        response = c.get('/incidents/?format=json')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()),1)
        self.assertEqual(response.json()[0]['incident'], "sample incident")
