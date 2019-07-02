from rest_framework import serializers


class CitizenSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateTimeField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    height = serializers.IntegerField()
    nationality = serializers.CharField()
    color_of_eyes = serializers.CharField()
