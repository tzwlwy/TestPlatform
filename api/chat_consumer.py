# consumers/chat_consumer.py
import asyncio

from core.consumers import BaseWebSocketConsumer


class ChatConsumer(BaseWebSocketConsumer):
    async def on_connect(self):
        print(f"用户 {self.user_id} 连接成功")

    async def on_message(self, data):
        msg = data.get("message")
        for i in range(10):
            await self.send_json({"echo": f"{msg} 第{i+1}次"})
            await asyncio.sleep(1)  # 每秒发送一次
