from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("message/", views.message_page, name= 'message')
]
