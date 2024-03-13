from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from mobile.models import Mobile


# Create your views here.

def mobiles(request):
    mobile_list = Mobile.objects.all().values()
    template = loader.get_template('books.html')
    context = {
        'mobiles': mobile_list,
    }
    return HttpResponse(template.render(context, request))
