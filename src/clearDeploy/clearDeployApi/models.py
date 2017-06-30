# python manage.py migrate --run-syncdb

from django.db import models
from django.utils import timezone


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
