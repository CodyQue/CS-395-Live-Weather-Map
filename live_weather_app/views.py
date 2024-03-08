from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
# Imports for the OpenWeather API
import requests
import json
from datetime import datetime


class travel_questionnaire(forms.Form):
    temp_opts = [
        ('accomodation', 'Hotels'),
        ('activity', 'Activities'),
        ('commercial', 'Shopping'),
        ('catering', 'Restaurants'),
        ('tourism', 'Tourism')
    ]
    max_dist = forms.CharField(label="Max distance (miles)")
    category = forms.ChoiceField(label='Category', widget=forms.RadioSelect, choices=temp_opts)


def get_geolocation():
    url = "https://api.geoapify.com/v1/ipinfo?&apiKey=09008c734555433dbf212c6c61ebea3b"
    resp = requests.get(url)
    return [resp.json()["location"]["latitude"], resp.json()["location"]["longitude"]]

def get_meters(miles):
    return round(miles*1609.34)

def get_places(lat, lon, category, max_dist):
    apiKey = "09008c734555433dbf212c6c61ebea3b"
    url = "https://api.geoapify.com/v2/places"
    params = {
        "categories": category,
        "limit": 5,
    }
    resp = requests.get(url)
    return resp.json()
    

def travel_advisor(request):
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    if request.method == "POST":
        form = travel_questionnaire(request.POST)
        if form.is_valid():
            categories = form.cleaned_data
            loc = get_geolocation()
            max_dist = form.cleaned_data["max_dist"]
            category = form.cleaned_data["category"]
            resp = get_places(loc[0], loc[1], category, int(max_dist))
            print(resp)
        # return HttpResponse()
    return render(request, "home/traveladvisor.html", {"form": travel_questionnaire()})


def map(request):
    API_KEY = 'cdac524628de1773c07153a946813a62'
    city_name = 'Fairfax'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()
    current_time = datetime.now()
    formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
    city_weather_update = {
        'city': city_name,
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'temperature': str(response['main']['temp']) + ' °C',
        'country_code': response['sys']['country'],
        'wind': str(response['wind']['speed']) + 'km/h',
        'humidity': str(response['main']['humidity']) + '%',
         'time': formatted_time
    }
    context = {'city_weather_update': city_weather_update}
    print(context)
    return render(request, 'home/index.html', context)
