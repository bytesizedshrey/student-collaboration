import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from .models import Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # new_room = Room(room_name=self.room_name)
        # new_room.save()
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)  # type: ignore

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)  # type: ignore

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["user"]
        context = {"message": message, "user": username}

        type(self.scope["user"])

        # Send message to room group
        await self.channel_layer.group_send(  # type: ignore
            self.room_group_name,
            {"type": "chat.message", "context": context},
        )

    # Receive message from room group
    async def chat_message(self, event):
        context = event["context"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"context": context}))
