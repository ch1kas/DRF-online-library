from rest_framework import serializers
from django.contrib.auth.models import AnonymousUser
from .models import Author, Genre, Book, Comment, Rating, Favorite

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'
    
class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
  user = serializers.ReadOnlyField(source='user.username')
  
  class Meta:
    model = Comment
    fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
  user = serializers.ReadOnlyField(source='user.username')
  
  class Meta:
    model = Rating
    fields = '__all__'
    
  def validate(self, data):
    request = self.context.get('request')
    if request and request.user:
      user = request.user
      book = data['book']
      if Rating.objects.filter(user=user, book=book).exists():
        raise serializers.ValidationError("You have already rated this book.")
    return data
    
  def validate_score(self, value):
    if value <0 or value > 5:
      raise serializers.ValidationError("Rating must be between 0 and 5")
    return value
    
class BookSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  genre = GenreSerializer()
  average_rating = serializers.SerializerMethodField()
  is_favorite = serializers.SerializerMethodField()
  comments = serializers.SerializerMethodField()
  ratings = serializers.SerializerMethodField()
  
  class Meta:
    model = Book
    fields = ['id', 'title', 'author', 'genre', 'average_rating', 'is_favorite', 'comments', 'ratings']
    
  def get_average_rating(self, obj):
    ratings = Rating.objects.filter(book=obj)
    if ratings.exists():
      return sum(rating.score for rating in ratings) / ratings.count()
    return 0

  def get_is_favorite(self, obj):
    user = self.context['request'].user
    if isinstance(user, AnonymousUser):
            return False
    return Favorite.objects.filter(book=obj, user=user).exists()

  def get_comments(self, obj):
      comments = Comment.objects.filter(book=obj)
      return CommentSerializer(comments, many=True).data

  def get_ratings(self, obj):
      ratings = Rating.objects.filter(book=obj)
      return RatingSerializer(ratings, many=True).data