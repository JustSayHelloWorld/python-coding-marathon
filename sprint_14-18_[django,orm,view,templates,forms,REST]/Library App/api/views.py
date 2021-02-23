from django.shortcuts import render
from .serializers import *
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from rest_framework import generics


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorSerializer


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorListSerializer
    queryset = Author.objects.all()


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class UserOrdersListView(generics.ListAPIView):
    serializer_class = UserOrdersListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Order.objects.filter(user=kwargs['user_id'])
        return self.list(request, *args, **kwargs)


