from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.map, name="map"),
    path('traveladvisor', views.travel_advisor, name="travel"),
    path('windmap',views.windmap, name = 'windmap' )
]
