from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.connection_pool import connection_pool
from core.utils.response import api_response


class ConnectionManager(APIView):
    def get(self, request, user_id=None):
        if user_id is None:
            # 返回所有用户连接和总数
            users = connection_pool.list_users()
            total_connections = connection_pool.count()
            return api_response(data={
                "total_connections": total_connections,
                "users": users,
            })
        else:
            return api_response(data={
                "total_connections": 1,
                "users": [user_id],
            })

    def delete(self, request, user_id=None):
        if user_id is None:
            return api_response(code=40001, message="user_id required for delete", http_status=status.HTTP_400_BAD_REQUEST)
        connection_pool.remove(user_id)
        return api_response(message=f"All connections for user {user_id} removed.")
