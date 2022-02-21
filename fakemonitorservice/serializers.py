from monitor.models import Incident
from rest_framework import serializers


class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incident
        fields = ['position', 'incident']