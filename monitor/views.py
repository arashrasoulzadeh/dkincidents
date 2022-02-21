from monitor.models import Incident,RemoteIncidentLog
from rest_framework import viewsets
from rest_framework import permissions
from monitor.serializers import IncidentSerializer
from django.http import HttpResponse
import requests
import json

class IncidentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Incident.objects.all().order_by( '-position' )
    serializer_class = IncidentSerializer


def FetchIncident( request ):
    id = RemoteIncidentLog.objects.count() + 1
    r = requests.get('http://localhost:8000/fake/{}'.format(id))
    if r.status_code == 200:
        if len(r.json()) > 0:
            ril = RemoteIncidentLog( response = r.text )
            ril.save()
            incident = Incident( incident=r.json()[0]['fields']['incident'])
            incident.save()
            return HttpResponse('saved')
    return HttpResponse( 'not found' )