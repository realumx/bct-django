from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="libraries")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
