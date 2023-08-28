from rest_framework import serializers
from .models import User, Role
from django.contrib.auth import authenticate


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



class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )


    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = "Unable to authenticate the user with given credentials"
            raise serializers.ValidationError(msg, code="authorization")
        
        attrs['user']= user
        return user