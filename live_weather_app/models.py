from django.db import models

# Model used for storing information of places in SQLite database
class Place(models.Model): 
    name = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length = 20)
    temperature = models.CharField(max_length = 20)
    wind = models.CharField(max_length = 20)
    humidity =models.CharField(max_length = 20)

    def __str__ (self):
        return f"Name: {self.name}, Description: {self.description}, Temperature: {self.temperature}, Wind: { self.wind }, Humidity: { self.humidity}"