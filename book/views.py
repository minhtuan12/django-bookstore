from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from book.models import Book


# Create your views here.


def books(request):
    book_list = Book.objects.all().values()
    template = loader.get_template('books.html')
    context = {
        'books': book_list,
    }
    return HttpResponse(template.render(context, request))
