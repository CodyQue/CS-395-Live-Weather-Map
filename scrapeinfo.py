import sqlite3
import requests
import time

count = 0

API_KEY = 'cdac524628de1773c07153a946813a62'
connection = sqlite3.connect("db.sqlite3")
cur = connection.cursor()
count = 0

with open('cities.txt', 'r', encoding='utf-8') as file:
    reader = file.readlines()
    for place in reader:
        i = place.replace('\n', '')
        #print(i)
        try:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={i}&appid={API_KEY}&units=metric'
            response = requests.get(url).json()
            project = (i, response['weather'][0]['description'], "test", "test")
            sql = '''INSERT INTO live_weather_app_place(name, description, temperature, wind, humidity, iconWeb, lat, long) VALUES(?,?,?,?,?,?,?,?)'''
            project = (i, response['weather'][0]['description'], str(response['main']['temp']) + ' °C', str(response['wind']['speed']) + 'km/h', str(response['main']['humidity']) + '%', "https://openweathermap.org/img/wn/" + response['weather'][0]['icon'] + "@2x.png", response['coord']['lat'], response['coord']['lon'])
            cur.execute(sql, project)
            connection.commit()
        except Exception as e:
            print(i, ", ", e)
            continue
        count += 1
        if (count >= 55):
            print("SLEEP")
            time.sleep(60)
            print("Wake up")
            count = 0


print('Done')