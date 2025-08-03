from bookshelf.models import Book

# Example: delete a book with id=1
try:
    book_to_delete = Book.objects.get(id=1)
    book_to_delete.delete()
    print("Book deleted successfully.")
except Book.DoesNotExist:
    print("Book not found.")
