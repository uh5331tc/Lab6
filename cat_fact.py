import requests

# data = requests.get('https://catfact.ninja/fact').json()

try:
    response = requests.get('https://catfact.ninja/fact')
    print(response.status_code)  #was it secessful or not
    print(response.text)  # prints the text of the repsonse
    print(response.json())  #


    data = response.json()  
    print(data)

    fact = data['fact']
    print(f'A Random cat fact: {fact} ')

except Exception as e: 
    print(e)
    print('There was an error making the request')