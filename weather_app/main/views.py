from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def weather(request):
    test = {
        'place': 'г. Москва',
        'temp': '32.1',
        'icon': '',
        'wind': 'N 3.1',
        'pressure': '772',
        'humidity': '50'
    }
    return render(request=request, template_name='main/index.html', context=test)


def about(request):
    return render(request=request, template_name='main/index.html')
