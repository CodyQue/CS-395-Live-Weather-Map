from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
# Imports for the OpenWeather API
import requests
import json
from datetime import datetime
# Imports for weather advisor
import numpy as np

class travel_questionnaire(forms.Form):
    temp_opts = [
        ('hot', 'Hot'),
        ('cold', 'Cold'),
        ('mild', 'Mild'),
    ]
    max_dist = forms.CharField(label="Max distance (miles)")
    temperature = forms.ChoiceField(label='Temperature', widget=forms.RadioSelect, choices=temp_opts)


def map(request):
    return render(request, 'home/index.html')

def travel_advisor(request):
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    if request.method == "POST":
        form = travel_questionnaire(request.POST)
        if form.is_valid():
            temperature = form.cleaned_data
            print(temperature)
            print()
        # return HttpResponse()
    return render(request, "home/traveladvisor.html", {"form": travel_questionnaire()})


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
