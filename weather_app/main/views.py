from django.shortcuts import render
from django.conf import settings
from requests import get

# Create your views here.


def weather(request):
    data = {
        'place': ' ',
        'temp': ' ',
        'temp_color': 'black',
        'icon': 'test',
        'wind': ' ',
        'wind_color': 'black',
        'pressure': ' ',
        'pressure_color': 'black',
        'humidity': ' ',
        'humidity_color': 'black',
    }
    if request.method == 'GET':
        # ! Работаем с геолокацией
        loc_holder = settings.GEOLOCATOR.geocode(settings.PLACE)
        data['place'] = [loc_holder.latitude, loc_holder.longitude]

        # ! Запрос в яндекс погоду
        response = get(
            settings.YANDEX_URL,
            headers={"X-Yandex-API-Key": settings.YANDEX_API_TOKEN},
            params={
                'lang': 'ru_RU',
                'limit': 7,
                'extra': True,
                'lat': data['place'][0],
                'lon': data['place'][1]
            }
        )

        # ! Отслеживание статуса
        if response.status_code == 200:
            response = response.json()
            data['temp'] = response['fact']['temp']
            data['wind'] = str(response['fact']['wind_dir']).capitalize() + ' ' + str(response['fact']['wind_speed'])
            data['pressure'] = response['fact']['pressure_mm']
            data['humidity'] = response['fact']['humidity']
            data['place'] = 'Россия, г. Москва'

            return render(
                request=request,
                template_name='main/index.html',
                context=data
            )
        else:
            return render(
                request=request,
                template_name='main/info.html',
                context={
                    'status': response.status_code,
                    'error': response.json,
                }
            )


def about(request):
    return render(request=request, template_name='main/index.html')
