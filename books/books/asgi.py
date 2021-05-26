"""
ASGI config for books project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
#oiriginal
import os
#add for chat
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
#original
from django.core.asgi import get_asgi_application
import messenger.routing

#original
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.settings')

# original 
# application = get_asgi_application()

#this portion of code modify for chat
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            messenger.routing.websocket_urlpatterns
        )
    ),
})
