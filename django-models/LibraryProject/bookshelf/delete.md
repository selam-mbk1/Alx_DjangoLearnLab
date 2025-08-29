from bookshelf.models import Book

# Retrieve the book by filtering on publication_year=1949
book = Book.objects.get(publication_year=1949)

# Delete the book
book.delete()

# Confirm deletion by retrieving all books again
books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []>
