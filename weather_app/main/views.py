from django.shortcuts import render

# Create your views here.


def weather(request):
    data = {
        'place': ' ',
        'temp': ' ',
        'icon': 'test',
        'wind': ' ',
        'pressure': ' ',
        'humidity': ' '
    }
    return render(request=request, template_name='main/index.html', context=data)


def about(request):
    return render(request=request, template_name='main/index.html')
