from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Comment, Rating, Favorite
from .serializers import BookSerializer, CommentSerializer, RatingSerializer


class BookListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['author__name', 'genre__name', 'date_published']
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
class BookDetailView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
class CommentListCreateView(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class RatingListCreateView(generics.ListCreateAPIView):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorites(request, pk):
  book = Book.objects.get(pk=pk)
  Favorite.objects.get_or_create(user=request.user, book=book)
  return Response({"message": "Book added to favorites"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_from_favorites(request, pk):
  book = Book.objects.get(pk=pk)
  favorite = Favorite.objects.filter(user=request.user, book=book)
  favorite.delete()
  return Response({"message": "Book removed from favorites"})