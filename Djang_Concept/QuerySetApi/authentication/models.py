from django.db import models

"""
Creating Custom Permissions on concrete modelc
"""
class Person(models.Model):
    class Meta:
        permissions = [("can_eat_pizzas", "Can eat pizzas"), ("can_get_pizzas", "Can get pizzas")]


"""
Creating Custom Permissions on proxy model, proxy model did not inherit concrete permissions
"""
class Student(Person):

    class Meta:
        proxy = True
        permissions = [("can_deliver_pizzas", "Can deliver pizzas")]
