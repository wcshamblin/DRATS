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
    queryset = WTB.objects.all()
    serializer_class = WTBSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class get_delete_update_movie(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

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
        serializer = WTBSerializer(req)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update WTB
    def put(self, request, pk):
        req = self.get_queryset(pk)
        if(request.user == req.creator): # If creator is who makes request
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
        if(request.user == req.creator): # If creator is who makes request
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
   
class get_post_WTBs(ListCreateAPIView):
    serializer_class = WTBSerializer    
    def get_queryset(self):
       WTBs = WTB.objects.all()
       return WTBs

    # Get all WTBs
    def get(self, request):
        WTBs = self.get_queryset()
        paginate_queryset = self.paginate_queryset(WTBs)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new WTB
    def post(self, request):
        serializer = WTBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)