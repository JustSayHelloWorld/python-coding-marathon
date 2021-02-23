from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='authors'),
    path('/<int:author_id>', detail, name='author'),
    path('/add_author', add_author, name='add_author'),
    path('add_author/<int:author_id>', add_author, name='add_author'),
    path('delete/<int:author_id>', del_author, name='del_author'),
]
