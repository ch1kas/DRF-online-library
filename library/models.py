from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Author(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name
  
class Genre(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  date_published = models.DateField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
  
class Comment(models.Model):
  book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
class Rating(models.Model):
  book = models.ForeignKey(Book, related_name='ratings', on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  
  class Meta:
    unique_together = ('user', 'book')
  
class Favorite(models.Model):
  book = models.ForeignKey(Book, related_name='favorites', on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
