from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CitizenSerializer


class CitizenView(APIView):
    view_type = "citizen"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CitizenSerializer(data=data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response("Inconsistent data", status=status.HTTP_400_BAD_REQUEST)
