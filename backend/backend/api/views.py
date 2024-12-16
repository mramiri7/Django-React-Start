from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from . models import Note


class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(author=user)
        return notes
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
 
            
class NoteDeleteView(generics.DestroyAPIView):

    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated)
    
    
    def get_queryset(self):
        user = self.request.user
        notes = Note.objects.filter(author=user)
        return notes


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[AllowAny]
