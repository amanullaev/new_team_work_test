from django.db import models
from app.models import *
from datetime import datetime


class TrenerModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='media/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'trener'