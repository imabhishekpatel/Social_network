from rest_framework import serializers
from user_management.models.customUserModel import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')