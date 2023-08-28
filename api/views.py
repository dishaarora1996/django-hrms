from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager, IsHR, IsEmployeeOrManager
from account.renderers import UserRenderer
from account.models import User 



# Create your views here.

class HolidayListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsHR]

    def post(self, request, format=None):
        text = request.data.get("data", None)
        if text:
            holiday = Holiday.objects.filter(name=text)
        else:
            holiday = Holiday.objects.all()
            
        serializer = HolidaySerializer(holiday, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class HREmployeeListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsHR]

    def get(self, request, format=None):
        user = User.objects.filter(is_onboarding=1)
        serializer = HREmployeeSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class HROnboardingListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsHR]

    def get(self, request, format=None):
        user = User.objects.filter(is_onboarding=0)
        serializer = HREmployeeSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class HRCompensationListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsHR]

    def get(self, request, format=None):
        user = User.objects.filter(is_onboarding=1)
        serializer = HRCompensationSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class HRProjectListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsHR]

    def get(self, request, format=None):
        project = Project.objects.all()
        serializer = HRProjectSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompensationDetailView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsEmployeeOrManager]

    def get(self, request, format=None):
        compensation = Compensation.objects.get(employee=request.user)
        serializer = CompensationSerializer(compensation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProjectListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsEmployeeOrManager]

    def get(self, request, format=None):
        project = Project.objects.filter(employee=request.user)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

class ClientListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request, format=None):
        client = Client.objects.filter(project__employee=request.user).order_by('name').distinct('name')
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ManagerEmployeeListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated, IsManager]

    filterset_fields = ['name']

    def get(self, request, format=None):
        emp_list=[]
        project = Project.objects.filter(employee=request.user)
        for i in project:
            employee = User.objects.filter(project=i).order_by('id').values()
            emp_list = {v['id']:v for v in employee}.values()

        serializer = EmployeeSerializer(emp_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)