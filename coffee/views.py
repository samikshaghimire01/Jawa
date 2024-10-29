
from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoffeeSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def home(request):
   coffee = Coffee.objects.all()
   return render(request, 'home.html' , {'coffee': coffee})


class CoffeeApi(APIView):
   permission_classes = [IsAuthenticated]
   def get(self, request):
      queryset = Coffee.objects.all()
      serializer = CoffeeSerializer(queryset, many=True)
      return Response({
         "status":True,
         "data": serializer.data
      })

      

class LoginAPI(APIView):
   def post(self, request):
      data = request.data 
      serializer = LoginSerializer(data=data)
      if not serializer.is_valid():
        return Response({
         "status":False,
         "data": serializer.errors
         })

      username = serializer.data['username']
      password = serializer.data['password'] 

      user_obj = authenticate(username = username, password = password)
   
      if user_obj:
         token , _ = Token.objects.get_or_create(user=user_obj)
         print (token.key)
      return Response({
         "status":True,
         "data": {'token' : str(token)}
         })
      return Response({
         "status":False,
         "data": {},
         "message": "Invalid Credential"

         })