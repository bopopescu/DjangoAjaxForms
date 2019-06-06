from rest_framework import serializers
from .models import LocalUsers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalUsers
        fields = '__all__'