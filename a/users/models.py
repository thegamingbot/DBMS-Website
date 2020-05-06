from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    ID =  models.CharField(primary_key=True, max_length = 4)
    Name = models.CharField(max_length = 64)
    Cost = models.IntegerField()

    def __str__(self):
        return f"{self.Name}"

class SelectedEvent(models.Model):
    Name = models.CharField(primary_key=True, max_length = 64)
    Events = models.ManyToManyField(Event, blank=True)
    Accomodation = models.BooleanField()

    def __str__(self):
        return f"{self.Name}"
