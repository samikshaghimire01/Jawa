from dataclasses import field
from rest_framework import serializers
from .models import Coffee

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields =  ['name']

class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()