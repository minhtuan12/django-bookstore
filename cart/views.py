from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from book.models import Book
from cart.cart import Cart


# Create your views here.

def cart_summary(request):
    template = loader.get_template('summary.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('book_id'))
        book = get_object_or_404(Book, id = book_id)
        cart.add(book = book)

        return "JsonReponse({'test': 'data'})"
