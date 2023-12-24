from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Drawing(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Session(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return f"{self.drawing.title} - Session"

