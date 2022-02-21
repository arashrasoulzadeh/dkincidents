from django.shortcuts import render
from fakemonitorservice.models import FakeIncident
# Create your views here.
from django.core import serializers
from django.http import HttpResponse


def FakeIncidents( request,position ):
    model = FakeIncident.objects.filter(position=position)
    jsonModel = serializers.serialize('json', model)
    return HttpResponse(jsonModel, content_type='application/json')