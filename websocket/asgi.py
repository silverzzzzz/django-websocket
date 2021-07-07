"""
ASGI config for websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

#application = get_asgi_application()
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter

from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
import main.routing

application = ProtocolTypeRouter( {
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack( URLRouter( main.routing.websocket_urlpatterns ) ),
} )
