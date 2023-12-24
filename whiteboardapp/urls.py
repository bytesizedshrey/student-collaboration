from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="whiteboard"),
    path("drawing/<int:drawing_id>/", views.drawing_detail, name="drawing_detail"),
]
