from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import WTBSerializer
from .models import WTB


class WTBViewSet(viewsets.ModelViewSet):
    queryset = WTB.objects.all().order_by('fname')
    serializer_class = WTBSerializer