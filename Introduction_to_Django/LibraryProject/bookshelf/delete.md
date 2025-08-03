# Delete

# Command: Delete the book you created (with publication_year=1949) and confirm deletion by retrieving all books again.

from bookshelf.models import Book
# Retrieve the book by filtering on publication_year=1949
book_to_delete = Book.objects.get(publication_year=1949)

# Delete the book
book_to_delete.delete()

# Confirm deletion by retrieving all books again
books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []>
