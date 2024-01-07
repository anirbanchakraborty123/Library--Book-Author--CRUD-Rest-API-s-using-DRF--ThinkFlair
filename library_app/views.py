from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import status
from rest_framework.response import Response

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def create(self, request, *args, **kwargs):
        author_id = request.data.get('author', None)
        if author_id:
            author = Author.objects.get(pk=author_id)
            if author.books.count() >= 5:
                return Response({'error': 'An author cannot have more than 5 books.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
