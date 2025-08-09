import os
import django
from book_shelf.models import Book

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Library, Librarian
Book.objects.filter(author=author)


# 1. Query all books by a specific author
author_name = "John Doe"
books_by_author = Author.objects.get(name=author_name).book_set.all()
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

# 2. List all books in a library
library_name = "Central Library"
library_books = Library.objects.get(name=library_name).books.all()
print(f"\nBooks in {library_name}:")
for book in library_books:
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
library_name = "Central Library"
librarian = Librarian.objects.get(library__name=library_name)
print(f"\nLibrarian for {library_name}: {librarian.name}")
