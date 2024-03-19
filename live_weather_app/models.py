from django.db import models

# Model used for storing information of places in SQLite database
class Place(models.Model): 
    name = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length = 20)
    temperature = models.CharField(max_length = 20)
    wind = models.CharField(max_length = 20)
    humidity =models.CharField(max_length = 20)
    iconWeb = models.CharField(max_length=100, default = "https://openweathermap.org/img/wn/10d@2x.png")
    lat = models.CharField(max_length = 20, default = "40")
    long = models.CharField(max_length = 20, default = "-74")
    lastUpdated = models.CharField(max_length = 100, default = "00:00:00") 
    windIcon = models.CharField(max_length=100, default = "strongwind.png")
    
    def __str__ (self):
        return f"Name: {self.name}, Description: {self.description}, Temperature: {self.temperature}, Wind: { self.wind }, Humidity: { self.humidity}, Icon: { self.iconWeb}, Lat: {self.lat}, Long: {self.long}"

class lastTimeUpdated(models.Model):
    date = models.CharField(max_length = 100, default = "00:00:00") 
    id = models.IntegerField(primary_key=True)

    def __str__ (self):
        return f"Last Updated: {self.date}"

class Lock(models.Model):
    lock = models.IntegerField()

    def __str__ (self):
        return f"Lock: {self.lock}"
