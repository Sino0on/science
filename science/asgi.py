import os

import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
django_asgi_app = get_asgi_application()
from channels.auth import AuthMiddlewareStack
import server.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'science.settings')


application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            server.routing.websocket_urlpatterns
        )
    )
})