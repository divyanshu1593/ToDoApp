from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Tasks(models.Model):
    desc = models.TextField()
    isDone = models.BooleanField(default=False)
    belongsTo = models.ForeignKey(Person, on_delete=models.CASCADE)