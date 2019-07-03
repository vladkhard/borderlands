from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import CitizenSerializer
from .models import Citizen


class CreateCitizenView(APIView):
    view_type = "citizen"

    def post(self, request):
        data = request.data
        serializer = CitizenSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(CitizenSerializer(instance=instance).data, status=status.HTTP_201_CREATED)
        return Response("Inconsistent data", status=status.HTTP_400_BAD_REQUEST)


class GetCitizenView(APIView):
    view_type = "citizen"

    def get(self, request, citizen_id):
        instance = get_object_or_404(Citizen, pk=citizen_id)
        return Response(CitizenSerializer(instance=instance).data, status=status.HTTP_200_OK)
