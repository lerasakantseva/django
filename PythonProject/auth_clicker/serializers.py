from .models import UserData
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id']

class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id', 'username', 'password']
