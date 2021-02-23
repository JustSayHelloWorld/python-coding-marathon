from rest_framework import serializers
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password', 'updated_at', 'created_at',
                  'role', 'is_active']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['surname', 'name', 'patronymic']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    authors = AuthorListSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')


class OrderListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['book', 'user', 'created_at', 'end_at', 'plated_end_at']


class UserOrdersListSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['book', 'created_at', 'end_at', 'plated_end_at']