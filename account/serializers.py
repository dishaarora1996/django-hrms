from rest_framework import serializers
from .models import User, Role



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    # role = serializers.RelatedField(read_only=True)
  
    class Meta:
        model = User
        fields = ['email', 'password']



