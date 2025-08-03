# Delete the book with id=1
book_to_delete = Book.objects.get(id=1)
book_to_delete.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()
print(books)
