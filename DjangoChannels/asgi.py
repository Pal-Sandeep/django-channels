"""
ASGI config for DjangoChannels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChannels.settings')

application = get_asgi_application()

ws_patterns = [
    path('test/', )
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})