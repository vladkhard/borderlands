from uuid import uuid4

from django.db import models

from .exceptions import WrongHeightError


class Citizen(models.Model):
    citizen_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateTimeField(blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=255, blank=False, null=False)
    height = models.IntegerField(blank=False, null=False)
    nationality = models.CharField(max_length=255, blank=False, null=False)
    color_of_eyes = models.CharField(max_length=255, blank=False, null=False)
