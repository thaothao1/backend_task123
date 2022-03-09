from datetime import datetime
from django.shortcuts import render
from django.contrib.auth import login
from rest_framework .response import Response
from rest_framework.views import APIView
from .models import CustomerUser
from rest_framework import generics , permissions
from .serializers import UserSerializer, UserSerializers , UserTokenSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer , UserTokenSerializer
from django.contrib.auth.hashers import check_password
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
import jwt , datetime
# Create your views here.
class Register(APIView):
    def post(self , request):
        serializer = UserSerializer(data= request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        users = CustomerUser.objects.filter(username= username).first()
        if users is None:
            raise AuthenticationFailed('User not found!')
        flash = check_password( password , users.password)
        if password != users.password:
            raise AuthenticationFailed('Incorrect password!')
        response = Response()
        response.data ={
            'message' : "success"
        }
        return response


class RegisterToken(generics.GenericAPIView):
    serializer_class = UserTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializers(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginToken(KnoxLoginView):
    permission_classes = ( permissions.AllowAny ,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginToken, self).post(request, format=None)


          