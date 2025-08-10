from django.db import models

# Author model - represents a book's author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name  # For readable display in admin and shell

# Book model - represents a book
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year book was published
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,  # If author is deleted, delete their books
        related_name='books'       # Allows reverse lookup: author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
