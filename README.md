# CS 395: Live Weather Map!
#### By Cody, Anthony, Sid, Abhay
Welcome! The objective of the website is to view different weather patterns around the world! The website consists of tracking the current temperature, wind speeds, and humidity percentages.

## Make sure a virtual environment is used:
It is required to use a virtual environment to run the web application (since the website requires using Django)

## Libraries Required
These are some of the external libraries used for the full-stack project:
- requests
- django-bootstrap-v5
- Django

All of the libraries are stored in *requirements.txt*. Use this command to install the necessary requirements:
#### `pip3 install -r requirements.txt`

Make sure you are in the *live_weather_app* directory to run the pip command.

## Running the web application on localhost
Make sure you are still in the *live_weather_app*. To host the web application locally, run this command:
#### `python manage.py runserver`

## API's Used / External Resources
For this project, there were three APIs used: OpenLayers, OpenWeather, GeoAPIfy.
- The OpenLayers API is used to display the map
- The OpenWeather API is used to fetch the current weather status of a specific place.
- The GeoAPIfy is used to fetch activities around places.

## Front-End
The front-end consists of HTML, CSS, and JavaScript. This is used to display the map (through an API call) onto the website, as well as navigation, action handling, and information posting.

## Back-End
The back-end consists of using Django and Python. This is used to fetch the data to be displayed onto the webpage. The back-end also consists of a program (running on another process when booting the server) that fetches data and puts it onto the database. This is used to display the place and their current weather condition on their map (weather icons, wind icons, humidity heat map).

## Database
This project utilizes SQLite3 to store/manage weather data. Data gets manipulated in the separate Python script, but data gets also added when a user finds a place that the database does not have.

## Features
The map is from Maptilers API which is a free, open source map for developers to use. Open Weather API is shown on the left of the map and displays the location's current weather information when searched. The Trip Advisor is shown under the weather information that provides possible places to visit.
![washingtonexample](https://github.com/CodyQue/CS-395-Live-Weather-Map/assets/156840927/366753da-ab4c-46bb-9d76-347b718e1994)


We repurposed an earthquake heat map to display humidity data instead. It is completed through the use of JavaScript and HTML to manipulate the visualization of the heat map. The data will keep updating dynamically and shows the most updated humidity levels.

![2024-03-2621-03-17-ezgif com-video-to-gif-converter (1)](https://github.com/CodyQue/CS-395-Live-Weather-Map/assets/156840927/db074a66-96c7-434d-b54e-985e2f350454)

The search bar features locations and gives some example places depending on the text given. If there were none listed, it will be added to the possible locations.

![2024-03-2621-14-59-ezgif com-video-to-gif-converter (1)](https://github.com/CodyQue/CS-395-Live-Weather-Map/assets/156840927/9bb225b0-0718-4960-91b8-d2811675fdc9)


### Sources used
<a href="https://thepythoncode.com/article/weather-app-django-openweather-api-using-python">Python Django Weather App Tutorial</a
>
<a href="https://developers.arcgis.com/openlayers/geocode-and-search/#:~:text=There%20is%20no%20direct%20integration%20with%20OpenLayers%20to,Set%20the%20API%20key%20to%20authenticate%20the%20request.">ArcGIS OpenLayers Geocode</a>

<a href="https://cloud.maptiler.com/maps/basic-v2/">MapTiler Map</a>

<a href="https://openweathermap.org/weather-conditions">OpenWeatherMap Conditions</a>

<a href="https://stackoverflow.com/questions/68360214/running-python-script-in-background-ec2">Running Python Script in Background on EC2</a>

<a href="https://www.youtube.com/watch?v=u0oEIqQV_-E&t=10s&ab_channel=ShobiPP">Python Weather App Tutorial</a>

<a href="https://icons8.com/icon/set/wind-level/group-ui">Wind Level Icons</a>

<a href="https://openlayers.org/en/latest/examples/heatmap-earthquakes.html">OpenLayers Heatmap</a>
