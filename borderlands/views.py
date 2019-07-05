from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.conf import settings

from .serializers import CitizenSerializer, PassingSerializer
from .models import Citizen


class CreateCitizenView(APIView):
    view_type = "citizen"

    def post(self, request):
        data = request.data
        serializer = CitizenSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(CitizenSerializer(instance=instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CitizenView(APIView):
    view_type = "citizen"

    def get(self, request, citizen_id):
        instance = get_object_or_404(Citizen, pk=citizen_id)
        return Response(CitizenSerializer(instance=instance).data, status=status.HTTP_200_OK)

    def patch(self, request, citizen_id):
        instance = get_object_or_404(Citizen, pk=citizen_id)
        data = CitizenSerializer(instance=instance).data
        data.update(request.data)
        serializer = CitizenSerializer(instance=instance, data=data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(CitizenSerializer(instance=instance).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, citizen_id):
        data = request.data
        serializer = PassingSerializer(data=data)
        if serializer.is_valid():
            passing = serializer.save()
            citizen = get_object_or_404(Citizen, pk=citizen_id)
            citizen.passings.append(passing)
            citizen.save()
            return Response(PassingSerializer(instance=passing).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)


class LastCitizenView(APIView):
    view_type = 'citizen'

    def get(self, request):
        if Citizen.objects.exists():
            last = Citizen.objects.last()
            return Response(CitizenSerializer(instance=last).data, status=status.HTTP_200_OK)
        return Response("There is no data yet", status=status.HTTP_404_NOT_FOUND)


class ListCitizenView(ListAPIView):
    view_type = 'citizen'
    serializer_class = CitizenSerializer

    def get_queryset(self):
        return Citizen.objects.all()

    def filter_queryset(self, queryset):
        if queryset.exists():
            q = Q()
            for key, value in self.request.query_params.items():
                if key in settings.ALLOWED_QUERY_PARAMS:
                    q &= Q(**{f"{key}__icontains": value})
            queryset = queryset.filter(q)
        return queryset
