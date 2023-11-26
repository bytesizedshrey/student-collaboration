from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=200)
    def __str__(self):
        return self.room_name


class Messages(models.Model):
    room_name = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True, max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ":-" + self.message + "//" + str(self.created)
