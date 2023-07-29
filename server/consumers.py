import datetime
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import *


class ChatConsumers(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope["url_route"]["kwargs"]["pk"]
        print(self.room_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        print(self.channel_name)
        text_data_json = json.loads(text_data)
        print(text_data_json)


        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'result': text_data_json,

            }
        )

    def chat_message(self, event):
        print(event)
        # message = event['message']
        # user_id = event["user"]
        # print(user_id)
        # user = get_object_or_404(Account, id=user_id)
        # mess = message
        # now = datetime.datetime.now()

        self.send(text_data=json.dumps(
            event
        ))
