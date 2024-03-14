from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
# Imports for the OpenWeather API
import requests
import json
from datetime import datetime
from .models import Place

class NewCity(forms.Form):
    cityInput = forms.CharField(label='cityInput', max_length=100)

def get_geolocation(): # gets user ip and finds location. 
    url = "https://api.geoapify.com/v1/ipinfo?&apiKey=09008c734555433dbf212c6c61ebea3b"
    resp = requests.get(url)
    return [resp.json()["location"]["latitude"], resp.json()["location"]["longitude"]]

def get_weather_info(city):
    API_KEY = 'cdac524628de1773c07153a946813a62'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()
    global city_weather_update 
    city_weather_update = {
        'city': city,
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'temperature': str(response['main']['temp']) + ' °C',
        'country_code': response['sys']['country'],
        'wind': str(response['wind']['speed']) + 'km/h',
        'humidity': str(response['main']['humidity']) + '%',
        'time': datetime.now().strftime("%A, %B %d %Y, %H:%M:%S %p"),
        'lon' : response['coord']['lon'],
        'lat' : response['coord']['lat'],
        'iconWeb' : "https://openweathermap.org/img/wn/" + response['weather'][0]['icon'] + "@2x.png",
    }

def map(request):
    if not request.method == "POST":
        get_weather_info('Fairfax')

    else:
        form = NewCity(request.POST)
        if form.is_valid():
            cityInput = form.cleaned_data["cityInput"]
            get_weather_info(cityInput)
    list_places = travel_advisor()
    context = {
        "city_weather_update": city_weather_update,
        "place" : Place.objects.all(),
        "list_places": list_places
    }
    print(context)
    return render(request, 'home/index.html', context)

def get_place_id(city):
    url = f"https://api.geoapify.com/v1/geocode/search?text={city}&format=json&apiKey=09008c734555433dbf212c6c61ebea3b"
    resp = requests.get(url)
    return resp.json()["results"][0]["place_id"]

def travel_advisor():
    list_places = []
    curr_city = city_weather_update["city"]
    city_id = get_place_id(curr_city)
    print(city_id)
    resp = get_places(city_id)
    for i in resp["features"]:
        list_places.append(i["properties"]["name"])
    return list_places

def get_places(place_id):
    apiKey = "09008c734555433dbf212c6c61ebea3b"
    url = f"https://api.geoapify.com/v2/places?categories=tourism&filter=place:{place_id}&limit=5&apiKey={apiKey}"
    resp = requests.get(url)
    return resp.json()