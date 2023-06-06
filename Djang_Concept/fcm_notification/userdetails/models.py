from django.db import models

from fcm_notification.base_model import Person

# Create your models here.
class UserDetails(Person):
    phone = models.CharField(max_length=16, db_column="PHONE", null=True, blank=True, default=None)