'''You must continue to run the program from bash to maintain the 
virtual enviornment.  type this: python current_weather.py'''

import requests
from pprint import pprint
import os

key = os.environ.get('WEATHER_KEY')
print(key)

city = input('Enter the city: ')
country = input('Enter the 2 letter country code: ')

location = f'{city},{country}'
#url = f'https://api.openweathermap.org/data/2.5/weather?q=minneapolis,mn,us&units=imperial&appid={key}'

# OR add additonal data to a variable to be more private 
url = 'https://api.openweathermap.org/data/2.5/weather?'
#Set location
#query = {'q': 'minneapolis, mn, usa', 'units': 'imperial', 'appid': key}

query = {'q': location, 'units': 'imperial', 'appid': key}

data = requests.get(url, params=query).json()

pprint(data)

temp = data['main']['temp'] #accessing the data we need

print(f'The current temperature is {temp} F')