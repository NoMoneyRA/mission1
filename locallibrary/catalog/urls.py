from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import BorrowBookView, BookCreateView, BookUpdateView, BookDeleteView, add_beloved_book

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),