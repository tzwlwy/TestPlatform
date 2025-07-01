
# socket路由

from django.urls import re_path

from api.chat_consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/api/chat/(?P<user_id>\w+)/$', ChatConsumer.as_asgi()),
]
