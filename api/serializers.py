from rest_framework import serializers
from .models import *



class HolidaySerializer(serializers.ModelSerializer):
  class Meta:
    model = Holiday
    fields = '__all__'


class HREmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ('is_onboarding', 'updated_at' )
