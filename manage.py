#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import sqlite3
import requests
import time
from datetime import datetime
from multiprocessing import Process

def getWindIcon(item):
    if item < 12:
        return 'lightwind.png'
    elif item >= 12 and item < 39:
        return 'moderatewind.png'
    else:
        return 'strongwind.png'

def scrapeInfoToDB():
    API_KEY = 'cdac524628de1773c07153a946813a62'
    while(True):
        print('Start')
        connection = sqlite3.connect("db.sqlite3")
        cur = connection.cursor()

        #Updates last time the database was updated
        deleteFromTimesTable = '''UPDATE live_weather_app_lasttimeupdated
        SET date = ?
        WHERE id = 1'''
        project = (datetime.now().strftime("%A, %B %d %Y, %H:%M:%S %p"),)
        cur.execute(deleteFromTimesTable, project)

        #Counts all instances
        project = "SELECT * FROM live_weather_app_place"
        cur.execute(project)
        items = list(cur.fetchall())
        #print("Total instances in the table:", items)
        count = 0
        for item in items:
            i = item[0]
            url = f'https://api.openweathermap.org/data/2.5/weather?q={i}&appid={API_KEY}&units=metric'
            response = requests.get(url).json()
            #print(i)
            try:
                windIcon = getWindIcon(response['wind']['speed'])
                #print("WindIcon: ", windIcon)
                sql = '''INSERT INTO live_weather_app_place(name, description, temperature, wind, humidity, iconWeb, lat, long, lastUpdated, windIcon) VALUES(?,?,?,?,?,?,?,?,?,?)'''
                project = (i, response['weather'][0]['description'], str(response['main']['temp']) + ' °C', str(response['wind']['speed']) + 'km/h', str(response['main']['humidity']) + '%', "https://openweathermap.org/img/wn/" + response['weather'][0]['icon'] + "@2x.png", response['coord']['lat'], response['coord']['lon'], datetime.now().strftime("%A, %B %d %Y, %H:%M:%S %p"), windIcon)
                cur.execute(sql, project)
                connection.commit()
            except Exception as e:
                #print(i, ", ", e)
                if 'UNIQUE constraint failed:' in str(e):
                    #print("Unique constraint")
                    windIcon = getWindIcon(response['wind']['speed'])
                    #print("WindIcon: ", windIcon)
                    sql = '''
                    UPDATE live_weather_app_place
                    SET description = ?,
                    temperature = ?,
                    wind = ?,
                    humidity = ?,
                    iconWeb = ?,
                    lastUpdated = ?,
                    windIcon = ?
                    WHERE name = ?;
                        '''
                    #print("HAS UNIQUE")
                    project = (response['weather'][0]['description'], str(response['main']['temp']) + ' °C', str(response['wind']['speed']) + 'km/h', str(response['main']['humidity']) + '%', "https://openweathermap.org/img/wn/" + response['weather'][0]['icon'] + "@2x.png", datetime.now().strftime("%A, %B %d %Y, %H:%M:%S %p"), windIcon, i)
                    cur.execute(sql, project)
                    connection.commit()
                    #print(count)
                else:
                    print("Error: ", e)
            count += 1
            if (count >= 55):
                #print("SLEEP")
                time.sleep(60)
                #print("Wake up")
                count = 0
        time.sleep(120)
        connection.close()
        print("GOES AGAIN")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'live_weather_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    p1 = Process(target=scrapeInfoToDB) # This runs the Python back-end program on a separate process (this is used to fetch data and put it onto the DB)
    p1.start()
    main()
