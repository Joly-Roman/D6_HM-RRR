from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('friends', FriendList.as_view(), name='friend_list'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('book/create', BookEdit.as_view(), name='book_create'),
    path('books', BookList.as_view(), name='book_list')
]