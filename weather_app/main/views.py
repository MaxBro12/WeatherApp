from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def weather(request):
    return render(request=request, template_name='main/index.html')


def about(request):
    return render(request=request, template_name='main/index.html')
