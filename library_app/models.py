from django.db import models

# Create your models here.

class Author(models.Model):
    """ AUTHOR TABLE """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name
        

class Book(models.Model):
    """ BOOK TABLE """
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

