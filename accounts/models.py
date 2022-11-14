from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    roll = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    sem = models.IntegerField()
    program = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ['roll']

    @property
    def first_name(self):
       return self.name.split(' ')[0]

    def __str__(self):
        return self.name