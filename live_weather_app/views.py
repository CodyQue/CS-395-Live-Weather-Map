from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Imports for the OpenWeather API
import requests
import json
from datetime import datetime

def map(request):
    API_KEY = 'cdac524628de1773c07153a946813a62'
    city_name = 'Paris'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()
    current_time = datetime.now()
    formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
    city_weather_update = {
        'city': city_name,
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
        'country_code': response['sys']['country'],
        'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
        'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
         'time': formatted_time
    }
    context = {'city_weather_update': city_weather_update}
    print(context)
    return render(request, 'home/index.html', context)