from datetime import datetime

from django.db import models


class Student(models.Model):
    name= models.CharField(max_length=254)
    roll = models.IntegerField(null=False)
    city = models.CharField(max_length=254)
    marks = models.IntegerField()
    pass_date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name

student = Student()




class Teacher(models.Model):
    name= models.CharField(max_length=254)
    empnum = models.IntegerField(null=False)
    city = models.CharField(max_length=254)
    salary = models.IntegerField()
    join_date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name