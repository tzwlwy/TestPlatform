# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import STPlatform.routing  # 替换为你的应用名

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'STPlatform.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            STPlatform.routing.websocket_urlpatterns
        )
    ),
})