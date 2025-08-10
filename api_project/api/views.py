from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()      # Get all Book records
    serializer_class = BookSerializer  # Use BookSerializer to convert data

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can create/update/delete; anyone can read
    permission_classes = [IsAuthenticatedOrReadOnly]