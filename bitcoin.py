import requests
from pprint import pprint 


try:
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    
    response = requests.get(coindesk_url)
    data = response.json()  
    pprint(data)

    dollars_exchange_rate = data['bpi'] ['USD']['rate_float']  #getting objects from the website 
    print(dollars_exchange_rate)

    bitcoin = float(input('Enter the amount of bitcoin you have: '))

    bitcoin_value_USD = bitcoin * dollars_exchange_rate

    print(f'Your {bitcoin} is equal to ${bitcoin_value_USD} in USD')

except Exception as e: 
    print(e)
    print('There was an error making the request')