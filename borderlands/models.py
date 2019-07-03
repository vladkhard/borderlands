from uuid import uuid4

from django.db import models

from .exceptions import WrongHeightError


class Marriage(models.Model):
    is_married = models.BooleanField(null=False)
    spouse_id = models.UUIDField(null=True)


class Citizen(models.Model):
    class Meta:
        ordering = ('last_name',)
    
    citizen_id = models.UUIDField(primary_key=True, default=lambda: uuid4().hex, editable=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    marriage = models.OneToOneField(Marriage, on_delete=models.CASCADE, related_name='citizen', blank=False, null=False)
    phone_number = models.CharField(max_length=255, blank=False, null=False)
    height = models.IntegerField(blank=False, null=False)
    nationality = models.CharField(max_length=255, blank=False, null=False)
    color_of_eyes = models.CharField(max_length=255, blank=False, null=False)
