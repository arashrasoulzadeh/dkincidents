from django.db import models

# Create your models here.
class FakeIncident(models.Model):
    position = models.AutoField( primary_key = True )
    incident = models.CharField( max_length = 30 )
    def __str__(self):
        return self.incident