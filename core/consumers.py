# consumers/base.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from core.connection_pool import connection_pool

class BaseWebSocketConsumer(AsyncWebsocketConsumer):
    user_id = None

    async def connect(self):
        self.user_id = self.scope["url_route"]["kwargs"].get("user_id")
        await self.accept()
        connection_pool.add(self.user_id, self)
        await self.on_connect()

    async def disconnect(self, close_code):
        connection_pool.remove(self.user_id)
        await self.on_disconnect(close_code)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            await self.on_message(data)
        except Exception as e:
            await self.send(text_data=json.dumps({"error": str(e)}))

    async def send_json(self, data):
        await self.send(text_data=json.dumps(data))

    # 留给子类扩展
    async def on_connect(self):
        pass

    async def on_disconnect(self, close_code):
        pass

    async def on_message(self, data):
        pass
