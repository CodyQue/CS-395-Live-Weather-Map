from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

class travel_questionnaire(forms.Form):
    Options = [
        ('hot', 'Hot'),
        ('cold', 'Cold'),
        ('mild', 'Mild'),
    ]
    temperature = forms.ChoiceField(label='Temperature', widget=forms.RadioSelect, choices=Options)
    # temperature = forms.CharField(label="Temperature")


def map(request):
    return render(request, 'home/index.html')

def travel_advisor(request):
    if request.method == "POST":
        form = travel_questionnaire(request.POST)
        if form.is_valid():
            temperature = form.cleaned_data["temperature"]
            print(temperature)
        return HttpResponse()
    return render(request, "home/traveladvisor.html", {"form": travel_questionnaire()})