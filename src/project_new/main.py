from project_new.src.project_new.Class.APIClient import APIClient
from project_new.src.project_new.Class.WeatherClient import WeatherClient
from project_new.src.project_new.Class.Weather import WeatherDays
from project_new.src.project_new.Class.Weather import Weather


api_client = APIClient('https://api.open-meteo.com')

weather_client = WeatherClient(api_client)

latitude = input('Enter Latitude: ')
longitude = input('Enter Longitude: ')
days = input('Enter Days: ')