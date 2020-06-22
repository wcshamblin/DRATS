from django.shortcuts import render
from rest_framework import permissions
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import viewsets
from rest_framework import generics
from API.serializers import UserSerializer
from API.serializers import WTBSerializer
from .models import WTB
from django.shortcuts import get_object_or_404

class get_delete_update_WTB(RetrieveUpdateDestroyAPIView):
    def get_queryset(self, pk):
        try:
            req = WTB.objects.get(pk=pk)
        except WTB.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return req

    # Get WTB
    def get(self, request, pk):
        req = self.get_queryset(pk)
        if(request.user == req.owner): # If owner is the one who requested
            serializer = WTBSerializer(req)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


    # Update WTB
    def put(self, request, pk):
        req = self.get_queryset(pk)
        if(request.user == req.owner): # If owner is the one who requested
            serializer = WTBSerializer(req, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete WTB
    def delete(self, request, pk):
        req = self.get_queryset(pk)
        if(request.user == req.owner): # If owner is the one who requested
            req.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   
class post_WTB(ListCreateAPIView):
    # NO GET HERE UNLESS ADMIN
    def get(self, request):
        if request.user.has_perm('API.view-all'):
            WTBs = WTB.objects.all()
            serializer = WTBSerializer(WTBs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        content = {
            'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)
    # Create a new WTB
    def post(self, request):
        serializer = WTBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data["idstr"], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)