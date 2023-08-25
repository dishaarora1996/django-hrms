from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from account.renderers import UserRenderer
from account.models import User 



# Create your views here.

class HolidayListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        holiday = Holiday.objects.all()
        serializer = HolidaySerializer(holiday, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class HREmployeeListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.filter(is_onboarding=1)
        serializer = HREmployeeSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)