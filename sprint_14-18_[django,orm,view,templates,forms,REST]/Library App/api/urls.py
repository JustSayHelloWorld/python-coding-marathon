from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/create', UserCreateView.as_view()),
    path('user/list', UserListView.as_view()),
    path('user/detail/<int:pk>/', UserDetailView.as_view()),
    path('author/create', AuthorCreateView.as_view()),
    path('author/list', AuthorListView.as_view()),
    path('author/detail/<int:pk>/', AuthorDetailView.as_view()),
    path('book/create', BookCreateView.as_view()),
    path('book/list', BookListView.as_view()),
    path('book/detail/<int:pk>/', BookDetailView.as_view()),
    path('order/create', OrderCreateView.as_view()),
    path('order/list', OrderListView.as_view()),
    path('order/detail/<int:pk>/', OrderDetailView.as_view()),
    path('user/<user_id>/order/', UserOrdersListView.as_view()),
    ]