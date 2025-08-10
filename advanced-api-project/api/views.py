from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework




class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Step 1: Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Step 2: Searching fields
    search_fields = ['title', 'author']

    # Step 3: Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering