import requests
import math

city_name = "montevideo"
api_key = "4630bf4acbe9679c0a98217c6be2201e"
constant_kelvin = 273.15

def get_weater(api_key, city):
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
   response = requests.get(url).json()

   temperature = response['main']['temp']
   temperature = (round(temperature  - constant_kelvin))
   feels_like = response['main']['feels_like']
   feels_like = (round(feels_like  - constant_kelvin))

   temperature = str(temperature)
   feels_like = str(feels_like)


   result = "La termperatura en: "+ city + " es de : " + temperature +" grados"+ " y se siente como si estuvieramos a " + feels_like + " grados"
   return result





