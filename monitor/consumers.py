import json
from channels.generic.websocket import WebsocketConsumer
from monitor.models import Incident
from monitor.serializers import IncidentSerializer
from django.core import serializers
from threading import Event, Thread
import time



class ChatConsumer(WebsocketConsumer):

    def ping(self):
        data = Incident.objects.all().order_by( '-position' ) 
        self.send( serializers.serialize('json',data) )

    def connect(self):
        self.accept()
        self.connected = True
        print( 'user connected' )
        starttime = time.time()
        while self.connected:
            self.ping()
            time.sleep(1.0 - ((time.time() - starttime) % 1.0))


    def disconnect(self, close_code):
        self.connected = False
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
