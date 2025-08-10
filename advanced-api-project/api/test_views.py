from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Create an author
        self.author = Author.objects.create(name="Jane Austen")
        
        # URL for the list of books
        self.list_url = reverse('book-list')  # use your actual url name

    def test_create_book(self):
        self.client.login(username='testuser', password='testpass')  # Login the user
        data = {
            "title": "Pride and Prejudice",
            "publication_year": 1813,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Pride and Prejudice")

    def test_list_books(self):
        Book.objects.create(title="Emma", publication_year=1815, author=self.author)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        book = Book.objects.create(title="Old Title", publication_year=1800, author=self.author)
        self.client.login(username='testuser', password='testpass')
        update_url = reverse('book-detail', kwargs={'pk': book.id})
        data = {"title": "New Title", "publication_year": 1800, "author": self.author.id}
        response = self.client.put(update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "New Title")

    def test_delete_book(self):
        book = Book.objects.create(title="Delete Me", publication_year=1800, author=self.author)
        self.client.login(username='testuser', password='testpass')
        delete_url = reverse('book-detail', kwargs={'pk': book.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
