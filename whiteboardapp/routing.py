from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/drawing/(?P<drawing_id>\d+)/$", consumers.DrawingConsumer.as_asgi()),
]
