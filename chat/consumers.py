import json
from channels.generic.websocket import AsyncWebsocketConsumer

#TODO: fix sending of data to include all the stuff and types given


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_type = text_data_json['type']
        user = text_data_json['user']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': message_type,
                'user': user,
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        message_type = event['type']
        user = event['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'type': message_type,
            'user': user,

        }))

    # Receive video from room group
    async def video_load(self, event):
        message = event['message']
        message_type = event['type']
        user = event['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'type': message_type,
            'user': user,

        }))
