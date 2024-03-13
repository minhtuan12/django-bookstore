import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from book import views
from django.http import JsonResponse
import string

from book.models import Book

import speech_recognition
import pyttsx3

from mobile.models import Mobile

recognizer = speech_recognition.Recognizer()
GOOGLE_CLOUD_CREDENTIALS = os.path.join(settings.BASE_DIR, 'django-416316-c02e277de9df.json')


# Create your views here.

def search_books(request):
    searched = []
    template = loader.get_template('search_books.html')
    books_template = loader.get_template('books.html')

    if request.method == 'POST':
        searched = request.POST['search_input']
        if searched != "":
            searched_books = Book.objects.filter(title__icontains = searched)
            context = {
                'searched': searched,
                'searched_books': searched_books
            }
            return HttpResponse(template.render(context, request))
        return views.books(request)
    return HttpResponse(books_template.render({}, request))


def search_book_by_voice(request):
    template = loader.get_template('search_books.html')
    books_template = loader.get_template('books.html')
    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source = source, duration = 0.2)
            audio = recognizer.listen(source = source)

            text = recognizer.recognize_google_cloud(audio, credentials_json = GOOGLE_CLOUD_CREDENTIALS)
            text = string.capwords(text)

            if text is not None:
                searched_books = Book.objects.filter(title__icontains = text)
                context = {
                    'searched': text,
                    'searched_books': searched_books
                }
                return HttpResponse(template.render(context, request))
    except speech_recognition.UnknownValueError:
        print("Could not understand")
        return HttpResponse(books_template.render({}, request))
    except speech_recognition.RequestError as e:
        print("Error requesting speech recognition service:", e)
        return HttpResponse(books_template.render({}, request))


def search_books_by_image(request):
    template = loader.get_template('search_books.html')
    books_template = loader.get_template('books.html')
    if request.method == 'POST' and request.FILES['image']:
        books = Book.objects.all()
        upload_image = request.FILES['image']
        save_uploaded_image(upload_image)
        return HttpResponse(books_template.render({}, request))
    return HttpResponse(books_template.render({}, request))


def save_uploaded_image(uploaded_image):
    # Xác định đường dẫn đến thư mục static
    static_dir = settings.STATIC_ROOT

    # Tạo một đường dẫn đến thư mục lưu trữ tệp ảnh trong thư mục static
    images_dir = os.path.join(static_dir, 'images/books')

    # Kiểm tra xem thư mục images đã tồn tại chưa, nếu chưa thì tạo mới
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Xác định đường dẫn đến tệp ảnh trong thư mục images
    image_path = os.path.join(images_dir, uploaded_image.name)

    # Lưu tệp ảnh vào thư mục images
    with open(image_path, 'wb') as destination:
        for chunk in uploaded_image.chunks():
            destination.write(chunk)

    # Trả về đường dẫn tới tệp ảnh đã lưu
    return image_path
