from datetime import datetime

from django.db import models


class Student(models.Model):
    name= models.CharField(max_length=254)
    roll = models.IntegerField(null=False, unique=True)
    city = models.CharField(max_length=254)
    marks = models.IntegerField()
    pass_date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name
