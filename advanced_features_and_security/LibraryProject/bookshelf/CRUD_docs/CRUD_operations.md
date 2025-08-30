from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Create Operation
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)