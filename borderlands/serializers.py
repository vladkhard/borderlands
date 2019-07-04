from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Citizen, Marriage


class MarriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marriage
        exclude = ('id',)

    def validate(self, validated_data):
        if validated_data["is_married"]:
            if "spouse_id" not in validated_data:
                raise ValidationError("If citizen is married data should contain spouse_id")
        return validated_data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if "spouse_id" in data and data["spouse_id"]:
            data["spouse_id"] = instance.spouse_id.hex
        return data


class CitizenSerializer(serializers.ModelSerializer):
    marriage = MarriageSerializer()

    class Meta:
        model = Citizen
        fields = '__all__'


    def create(self, validated_data):
        marriage_data = validated_data.pop("marriage")
        citizen = Citizen(**validated_data)
        citizen.save()
        marriage = Marriage(citizen=citizen, **marriage_data)
        marriage.save()
        citizen.marriage = marriage
        citizen.marriage_id = marriage.id
        citizen.save()
        return citizen

    def update(self, instance, validated_data):
        marriage_data = validated_data.pop("marriage")
        if marriage_data:
            serializer = MarriageSerializer(instance=instance.marriage, data=marriage_data)
            if serializer.is_valid():
                serializer.save()
                instance.marriage = serializer.instance
        return super().update(instance, validated_data)

    def validate(self, validated_data):
        marriage = validated_data.get("marriage")
        if marriage:
            cid = self.instance.citizen_id if self.instance else None
            spouse = Citizen.objects.filter(pk=marriage["spouse_id"])
            if not spouse.exists():
                raise ValidationError("Spouse id must exist")
            spouse = spouse.first()
            if cid == spouse.citizen_id:
                raise ValidationError("Citizen could not be married with himself")
        return validated_data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not isinstance(data["citizen_id"], str):
            data["citizen_id"] = instance.citizen_id.hex
        return data
