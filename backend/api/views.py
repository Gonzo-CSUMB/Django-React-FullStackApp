from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # only authenticated users can access this view, valid JWT token is required

    def get_queryset(self):
        user = self.request.user # get the user who made the request
        return Note.objects.filter(author=user) # get all notes created by this user

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # only authenticated users can access this view, valid JWT token is required

    def get_queryset(self):
        user = self.request.user # get the user who made the request
        return Note.objects.filter(author=user) # get all notes created by this user
    
    

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # get all users, this is used to query against
    serializer_class = UserSerializer
    permission_classes = (AllowAny,) # allow any user to create a user

