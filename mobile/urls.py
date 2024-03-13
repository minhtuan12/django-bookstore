from django.urls import path
from mobile import views

urlpatterns = [
    path('mobiles/', views.mobiles, name='mobiles'),
]
