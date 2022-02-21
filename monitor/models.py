from django.db import models

# Create your models here.
class Incident(models.Model):
    position = models.AutoField( primary_key = True )
    incident = models.CharField( max_length=144 )

    def __str__(self):
        return self.incident


class RemoteIncidentLog(models.Model):
    position = models.AutoField( primary_key = True )
    response = models.CharField( max_length=144 )
