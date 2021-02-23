from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='books'),
    path('<int:book_id>', detail, name='book'),
    path('add_book', add_book, name='add_book'),
    path('delete/<int:book_id>', del_book, name='del_book'),
    path('add_book/<int:book_id>', add_book, name='add_book'),

]
