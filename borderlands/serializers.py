from rest_framework import serializers

from .models import Citizen


class CitizenSerializer(serializers.Serializer):
    citizen_id = serializers.UUIDField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    height = serializers.IntegerField()
    nationality = serializers.CharField()
    color_of_eyes = serializers.CharField()
