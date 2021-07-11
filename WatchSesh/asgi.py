"""
ASGI config for WatchSesh project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
'''
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WatchSesh.settings")
application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
'''
import os
import django

def wrapperfunction1():
    import channels
    return channels.routing.get_default_application()



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WatchSesh.settings')

django.setup()

application = wrapperfunction1()

