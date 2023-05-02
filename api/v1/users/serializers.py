from users.models import *
from general.models import *
from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField(max_length=16)
    email = serializers.CharField()
    country = serializers.CharField()
    password = serializers.CharField()
