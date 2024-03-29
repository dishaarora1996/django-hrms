from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .renderers import UserRenderer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.
class UserLoginView(APIView):

    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login Success', 'name': user.name, 'email': user.email, 'designation': user.designation, 'role': user.role.name},
                                 status=status.HTTP_200_OK)
            else:
                return Response({'errors': 
                    'Email or Password is not valid'},
                    status=status.HTTP_404_NOT_FOUND)
            

# class CustomAuthToken(ObtainAuthToken):

#     # def post(self, request, *args, **kwargs):
#     #     serializer = AuthTokenSerializer(data=request.data)
#     #     if serializer.is_valid(raise_exception=True):
#     #         print(f"User*****************: {serializer.validated_data['user']}")
#     #         user = serializer.validated_data['user']
#     #         # token, created = Token.objects.get_or_create(user=user)
#     #         return Response({
#     #             'msg': 'OK',
#     #             'user': user.email
#     #         })
            
#     #     return Response({
#     #                 'msg': 'Not Valid'
#     #             })

#     """Create a new auth token for user"""
#     serializer_class = AuthTokenSerializer