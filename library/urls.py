from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookListView, BookDetailView, CommentListCreateView, RatingListCreateView, add_to_favorites, remove_from_favorites

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/comments/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('books/<int:pk>/ratings/', RatingListCreateView.as_view(), name='rating_list_create'),
    path('books/<int:pk>/favorite/', add_to_favorites, name='add_to_favorites'),
    path('books/<int:pk>/unfavorite/', remove_from_favorites, name='remove_from_favorites'),
]
