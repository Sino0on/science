import datetime
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import *
from .serializers import MessageSerializer


class ChatConsumers(WebsocketConsumer):
    def connect(self):
        print(self.scope["user"])
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
        message = Message.objects.create(
            text=text_data_json['result']['text'],
            sender=Person.objects.get(pk=text_data_json['result']['sender']),
            chat=Chat.objects.get(pk=self.room_group_name)
        )
        print(message)
        message_data = MessageSerializer(instance=message)


        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'result': message_data.data,

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

        # message = Message.objects.create(
        #     text=event["result"]['message']['text'],
        #     sender=Person.objects.get(pk=event["result"]['sender']),
        #     chat=Chat.objects.get(pk=self.room_group_name)
        # )
        # print(message)
        # message_data = MessageSerializer(instance=message)
        # print(message_data.data)
        self.send(text_data=json.dumps(
            event,
            ensure_ascii=False
        ))
