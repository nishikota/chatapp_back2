from rest_framework import serializers
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

class LoginSerializer(serializers.Serializer):
  username=None