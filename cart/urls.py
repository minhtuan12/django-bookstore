from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart_summary, name = 'cart'),
    path('cart/', views.cart_add, name = 'cart_add')
]
