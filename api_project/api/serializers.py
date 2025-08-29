from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book              # Use the Book model
        fields = '__all__'        # Serialize all fields of the model
