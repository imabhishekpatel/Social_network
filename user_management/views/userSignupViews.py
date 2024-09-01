
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from user_management.models.customUserModel import CustomUser

from rest_framework.response import Response
from rest_framework import generics
from user_management.serializers.userSerializer import UserSerializer
from django.db.models import Q
from rest_framework.views import APIView



class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'message': 'User created successfully'
        })
    