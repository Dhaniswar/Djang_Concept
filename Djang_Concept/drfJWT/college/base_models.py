from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=254, default=None, null=True, blank=True)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=254, default=None, null=True, blank=True)
    email = models.EmailField()

    class Meta:
        abstract= True

    
    def __str__(self):
        return self.name
