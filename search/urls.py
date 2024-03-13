from django.urls import path
from search import views

app_name = 'search'

urlpatterns = [
    path('search_books/', views.search_books, name = 'search_books'),
    path('search_books_by_voice/', views.search_book_by_voice, name = 'search_books_by_voice'),
    path('search_books_by_image/', views.search_books_by_image, name = 'search_books_by_image')
]
