from django.db import models

class Course(models.Model):
    course_id = models.IntegerField(null=True, default=None)
    duration = models.IntegerField(null=True, default=None)
    name = models.CharField(max_length=254, blank=True, null=True, default=None)
    fees = models.IntegerField(null=True, default=None)



    def __str__(self):
        return self.name
        