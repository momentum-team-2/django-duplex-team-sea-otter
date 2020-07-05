from django.db import models

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=55)
    goal = models.CharField(max_length=55)