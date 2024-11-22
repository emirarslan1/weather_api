#importing requests and json 
import requests
#base url
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "6bdaa6d751b8137dada9894156206951"
CITY = input('enter the city that you wanna see')
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = round(main['temp'] - 273.15 , 2 )
    print(temperature)
else:
    print(':/')