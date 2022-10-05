'''Noelle Bauer this program takes in user input to create a 5 day forecast. 
data is collected from the openweathermap.org source and then presented
to the user as a five day weather forecast'''

import requests
import os
from pprint import pprint
from datetime import datetime


def main():
    print('Welcome to the 5 day Weather Forecast, the perfect way to plan your dream vacation!')
    city = input('What city would you like? ')
    country = input('What is the name of the country? ')

    try:
        data = get_current_weather(city, country)

        if data:
            current_temp = extract_temperature(data)
            print(f'The current temperature in {city.title()}, {country.upper()} is {current_temp:.2f}F') #logging to user

        else:
            print('This location was not found.')

    except Exception as e:  # TODO handle different types of error
        print('Sorry, there was an error fetching data. '
              'Please check your internet connection, and if that\'s ok, report this to the developer.', e)



def get_current_weather(city, country):

    """ Query the Open Weather Map API for the current conditions for a city and country.
    Returns the JSON from Open Weather Map if the location is found
    Return None if the location is not found
    Raises an exception if connection error, API key error etc.
    """

    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    key = os.environ.get('WEATHER_KEY')
    assert key is not None # raises an error if environment variable is not set

    # Configure query parameters for the API
    location = '%s,%s' % (city, country)
    query = {'q': location, 'units': 'imperial', 'appid': key }

    # And make request...
    data = requests.get(base_url, params=query)
    
    list_of_forecast = data['list']
    for forecast in list_of_forecast:
        temp = forecast['main']['temp']
        timestamp = forecast['dt']
        forecast_date = datetime.fromtimestamp(timestamp)

    print(f' At {forecast_date} the temp will be {temp}F')


    # Status codes of 200 mean the request was received and processed without error
    if data.status_code == 200:
        return data.json()
    # The API returns 404 (Not Found) if the location can't be found. Check for this and return None
    if data.status_code == 404:
        return None

    # Any other errors, raise an exception
    data.raise_for_status()  # Raise an exception if the status code is not 2xx or 3xx


def extract_temperature(data):
    return data['main']['temp']



#print(time.time()) # Unix time
#print(datetime.fromtimestamp(1500000000)) 
# Convert timestamp to local time

if __name__ == '__main__':
    main()


