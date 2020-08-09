from django.db import models
from django.contrib.auth.models import User
import datetime


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=4000, default='', null=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

