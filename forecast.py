#Example URL
#https://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&appid=94a3cbdb9c352405bd892fe45a62e8e2

import os
import requests
from datetime import datetime
from pprint import pprint


key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key }


url = 'https://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
pprint(data)

list_of_forecast = data['list']

for forecast in list_of_forecast:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)

    print(f' At {forecast_date} the temp will be {temp}F')

