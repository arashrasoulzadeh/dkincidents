from django.contrib import admin
from monitor.models import Incident,RemoteIncidentLog
from fakemonitorservice.models import FakeIncident
# Register your models here.
admin.site.register(Incident)
admin.site.register(FakeIncident)
admin.site.register(RemoteIncidentLog)