from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Purchase

def index(request):
    return render(request, 'index.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def buy_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    Purchase.objects.create(book=book)
    return redirect('history')


def history(request):
    purchases = Purchase.objects.order_by('-purchased_at')
    return render(request, 'history.html', {'purchases': purchases})
