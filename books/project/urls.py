from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.books, name='books'),
    path('buy/<int:book_id>/', views.buy_book, name='buy_book'),
    path('history/', views.history, name='history'),
]