from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
# Imports for the OpenWeather API
import requests
import json
from datetime import datetime

class NewCity(forms.Form):
    cityInput = forms.CharField(label='cityInput', max_length=100)

class travel_questionnaire(forms.Form): # maybe add more categories?
    # idea for ML: have user enter category without options, use sklearn to 
    # match user entry to closest option the api takes. 
    temp_opts = [
        ('accommodation', 'Hotels'),
        ('activity', 'Activities'),
        ('commercial', 'Shopping'),
        ('catering', 'Restaurants'),
        ('tourism', 'Tourism')
    ]
    max_dist = forms.CharField(label="Max distance (miles)")
    category = forms.ChoiceField(label='Category', widget=forms.RadioSelect, choices=temp_opts)


def get_geolocation(): # gets user ip and finds location. 
    url = "https://api.geoapify.com/v1/ipinfo?&apiKey=09008c734555433dbf212c6c61ebea3b"
    resp = requests.get(url)
    return [resp.json()["location"]["latitude"], resp.json()["location"]["longitude"]]

def get_meters(miles): # literally just converts miles to meters. 
    return round(miles*1609.34)

def get_places(lat, lon, category, max_dist):
    limit = 10
    apiKey = "09008c734555433dbf212c6c61ebea3b"
    max_dist = get_meters(max_dist)
    url = f"https://api.geoapify.com/v2/places?categories={category}&filter=circle:{lon},{lat},{max_dist}&bias=proximity:{lon},{lat}&limit={limit}&apiKey={apiKey}"
    resp = requests.get(url)
    return resp.json()
    

def travel_advisor(request):
    i = 0
    list_places = []
    if request.method == "POST":
        form = travel_questionnaire(request.POST)
        if form.is_valid():
            loc = get_geolocation()
            print("Location: ", loc)
            max_dist = form.cleaned_data["max_dist"]
            category = form.cleaned_data["category"]
            resp = get_places(loc[0], loc[1], category, int(max_dist))
            feat = resp["features"]
            for i in range(len(feat)): # responses are not normalized, for now, just ignore if not returned in expected manner.
                try:
                    list_places.append(feat[i]["properties"]["name"])
                except KeyError:
                    continue
            print(list_places)
        # return render(request, "home/traveladvisor.html", {"list_places": list_places})
    return render(request, "home/traveladvisor.html", {"form": travel_questionnaire(), "list_places": list_places})


def map(request):
    API_KEY = 'cdac524628de1773c07153a946813a62'
    if request.method == "POST":
        form = NewCity(request.POST)
        if form.is_valid():
            cityInput = form.cleaned_data["cityInput"]
            city_name = cityInput 
            print(cityInput)
            print(form)
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            response = requests.get(url).json()
            print(response)
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
                'time': formatted_time,
                'lon' : response['coord']['lon'],
                'lat' : response['coord']['lat'],
            }
            context = {'city_weather_update': city_weather_update}
            print('MAP POSTED')
            return render(request, 'home/index.html', context)
    else:
        city_name = 'Fairfax'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
        response = requests.get(url).json()
        print(response)
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
            'time': formatted_time,
            'lon' : response['coord']['lon'],
            'lat' : response['coord']['lat'],
        }
        context = {'city_weather_update': city_weather_update}
        #print(context)
        return render(request, 'home/index.html', context)
