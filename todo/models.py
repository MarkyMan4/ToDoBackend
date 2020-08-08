from django.db import models
import datetime


class ToDo(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=4000, default='', null=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

