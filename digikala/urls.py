from django.contrib import admin
from django.urls import include, path
from monitor.views import IncidentViewSet
from rest_framework import routers
from django.views.generic.base import TemplateView
from fakemonitorservice.views import FakeIncidents
from monitor.views import FetchIncident

router = routers.DefaultRouter()
router.register(r'incidents', IncidentViewSet)

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.htm')),
    path('', include(router.urls)),
    path('fake/<int:position>', FakeIncidents),
    path('fetch', FetchIncident),
    path('admin/', admin.site.urls),
]
