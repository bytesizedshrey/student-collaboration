import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DrawingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.drawing_id = self.scope['url_route']['kwargs']['drawing_id']
        # Create a group specific to the drawing
        await self.channel_layer.group_add(    #type: ignore
            f'drawing_{self.drawing_id}',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove from the drawing group on disconnect
        await self.channel_layer.group_discard(     #type: ignore
            f'drawing_{self.drawing_id}',
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming WebSocket messages
        data_json = json.loads(text_data)
        # Process the received data (e.g., drawing updates)
        # Broadcast the processed data to other clients in the drawing group
        await self.channel_layer.group_send(    #type: ignore
            f'drawing_{self.drawing_id}',
            {
                'type': 'send_drawing_update',
                'data': data_json,
            }
        )

    async def send_drawing_update(self, event):
        # Send drawing updates to the WebSocket
        data = event['data']
        # Send the data to the WebSocket
        await self.send(text_data=json.dumps(data))
