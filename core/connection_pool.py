'''
连接池管理
'''
from collections import defaultdict

class ConnectionPool:
    def __init__(self):
        self.connections = defaultdict(set)  # user_id -> set of consumers

    def add(self, user_id, consumer):
        self.connections[user_id].add(consumer)

    def remove(self, user_id, consumer=None):
        if consumer:
            self.connections[user_id].discard(consumer)
        else:
            self.connections.pop(user_id, None)

    def get(self, user_id):
        return self.connections.get(user_id, set())

    def list_users(self):
        return list(self.connections.keys())

    def count(self):
        return len(self.connections)

    async def send_to_user(self, user_id, data: dict):
        for consumer in self.get(user_id):
            await consumer.send_json(data)


connection_pool = ConnectionPool()
