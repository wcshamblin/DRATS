from django.shortcuts import render
from rest_framework import permissions
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from API.serializers import UserSerializer
from API.serializers import WTBSerializer
from .models import WTB


class WTBViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WTB.objects.all().order_by('fname')
    serializer_class = WTBSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )