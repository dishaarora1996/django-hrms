from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'


class HolidaySerializer(serializers.ModelSerializer):
  class Meta:
    model = Holiday
    fields = '__all__'


class HREmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'name', 'email', 'designation', 'role', 'created_at']


class CompensationSerializer(serializers.ModelSerializer):


  class Meta:
    model = Compensation
    fields = ['id', 'ctc', 'basic', 'hra']

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ['id', 'name']

class HRCompensationSerializer(serializers.ModelSerializer):
  compensation_set = CompensationSerializer(many=True)
  class Meta:
    model = User
    fields = ['id', 'name', 'email', 'designation', 'role', 'created_at', 'compensation_set']
    related_object = 'compensation'


class HRProjectSerializer(serializers.ModelSerializer):
  # employee_set = EmployeeSerializer(many=True)

  employee = EmployeeSerializer(read_only=True, many=True)
  class Meta:
    model = Project
    fields = ['id', 'name', 'employee']

class ClientSerializer(serializers.ModelSerializer):

  class Meta:
    model = Client
    fields = ['id', 'name']

  

