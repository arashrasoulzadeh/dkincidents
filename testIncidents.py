from django.test import TestCase,Client
from monitor.models import Incident

class TestIncidents(TestCase):
    def setUp(self):
        pass

    def test_incident_is_inserted(self):
        Incident.objects.create( incident = "sample incident" )
        qs = Incident.objects.filter(position=1)
        self.assertEqual(len(qs),1)
        self.assertEqual(qs[0].incident, "sample incident" )