from django.db import models
from datetime import datetime
from app.models import CustomUser


class New(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)