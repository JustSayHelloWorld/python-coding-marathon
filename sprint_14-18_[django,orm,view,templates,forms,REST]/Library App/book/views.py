from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

from rest_framework import generics



def index(request):
    books = Book.objects.order_by('-id')
    return render(
        request,
        'book/index.html',
        {'title': 'Книги', 'books': books}
    )

def detail(request, book_id):
    book = Book.get_by_id(book_id)
    context = {
        'title': f'Книга "{book.name}"',
        'book': book
    }
    return render(
        request,
        'book/detail.html',
        context
    )

def add_book(request, book_id=0):
    if request.method == 'GET':
        if book_id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=book_id)
            form = BookForm(instance=book)
        return render(request, 'book/add_book.html', {'form': form})
    else:
        if book_id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=book_id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('books')

def del_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('books')

"""   Django REST methods   """
