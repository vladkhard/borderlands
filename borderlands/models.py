from uuid import uuid4
from datetime import datetime
import json

from djongo import models

from .exceptions import WrongHeightError


# seems a little hacky
# TODO: find better solution
class ListField(models.ListField):
    def to_python(self, value):
        if isinstance(value, str):
            try:
                value = value.replace("'", '"')
                value = json.loads(value)
            except json.decoder.JSONDecodeError:
                pass
        if not isinstance(value, list):
            raise ValueError(
                f'Value: {value} stored in DB must be of type list'
                'Did you miss any Migrations?'
            )
        return value


class Marriage(models.Model):
    is_married = models.BooleanField(null=False)
    spouse_id = models.UUIDField(null=True)


class Passing(models.Model):
    forbidden_stuff = ListField()
    status = models.BooleanField()
    date = models.DateTimeField(default=datetime.now)


class Citizen(models.Model):
    class Meta:
        ordering = ('creation_date',)
    
    citizen_id = models.UUIDField(primary_key=True, default=lambda: uuid4().hex, editable=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    marriage = models.OneToOneField(Marriage, on_delete=models.CASCADE, related_name='citizen', blank=False, null=False)
    passings = models.ArrayModelField(model_container=Passing, blank=False, null=False, default=[])
    phone_number = models.CharField(max_length=255, blank=False, null=False)
    height = models.IntegerField(blank=False, null=False)
    nationality = models.CharField(max_length=255, blank=False, null=False)
    color_of_eyes = models.CharField(max_length=255, blank=False, null=False)
    creation_date = models.DateTimeField(default=datetime.now)
