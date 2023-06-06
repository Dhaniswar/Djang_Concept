from django.db import models


class Person(models.Model):

    name = models.CharField(
        max_length=254,
        db_column="NAME",
        blank=True,
        null=True,
        default=None
    )

    age = models.CharField(
        max_length=254,
        db_column="AGE",
        blank=True,
        null=True,
        default=None
    )

    email = models.CharField(
        max_length=254,
        db_column="EMAIL",
        blank=True,
        null=True,
        default=None
    )

    address = models.CharField(
        max_length=254,
        db_column="ADDRESS",
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        abstract = True
