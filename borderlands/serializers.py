from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Citizen, Marriage


class MarriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marriage
        exclude = ('id', )

    def validate(self, validated_data):
        if validated_data["is_married"] and validated_data["spouse_id"] is None:
            raise ValidationError("If citizen is married data should contain spouse_id")
        return validated_data


class CitizenSerializer(serializers.ModelSerializer):
    marriage = MarriageSerializer()

    class Meta:
        model = Citizen
        fields = '__all__'

    def create(self, validated_data):
        marriage_data = validated_data.pop("marriage")
        citizen = Citizen(**validated_data)
        Marriage(citizen=citizen, **marriage_data)
        return citizen