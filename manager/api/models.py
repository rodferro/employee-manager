from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    department = models.CharField(max_length=30)