from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()      # Get all Book records
    serializer_class = BookSerializer  # Use BookSerializer to convert data

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Book instances.
    Provides list, create, retrieve, update, and delete actions.
    """
    queryset = Book.objects.all()            # Get all books
    serializer_class = BookSerializer  