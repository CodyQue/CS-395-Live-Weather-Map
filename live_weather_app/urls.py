from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.map, name="map"),
    path('windmap',views.windmap, name = 'windmap' ),
    path('humiditymap', views.humiditymap, name = 'humiditymap')
]
