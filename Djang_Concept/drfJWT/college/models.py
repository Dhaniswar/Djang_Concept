from django.db import models
from .base_models import Person

class Student(Person):
    section = models.CharField(max_length=254, default=None, null=True, blank=True)


