from project_new.src.project_new.Class.APIClient import APIClient
from project_new.src.project_new.Class.WeatherClient import WeatherClient
from project_new.src.project_new.Class.Weather import WeatherDays
from project_new.src.project_new.Class.Weather import Weather


api_client = APIClient('https://api.open-meteo.com')

weather_client = WeatherClient(api_client)

latitude = input('Enter Latitude: ')
longitude = input('Enter Longitude: ')
days = input('Enter Days: ')

if days == '1':
    temperature, wind_speed, wind_direction, weather_code = weather_client.get_current_weather(latitude, longitude)
    weather_1 = Weather(temperature, wind_speed, wind_direction, weather_code)

    print(f'\nCurrent weather\n'
          f'----------------\n'
          f'Temperature: {weather_1.temperature} °C\n'
          f'Wind speed: {weather_1.wind_speed} km/h\n'
          f'Wind direction: {weather_1.wind_direction}°\n'
          f'Weather code: {weather_1.weather_code}\n')
else:
    temperature, wind_speed, wind_direction, weather_code = weather_client.get_forecast(latitude, longitude, int(days))
    weather_days = WeatherDays(temperature, wind_speed, wind_direction, weather_code)

    print(f'\nCurrent weather {days}\n'
          f'----------------\n'
          f'Temperature MAX: {[el for el in weather_days.temperature_max]} °C\n'
          f'Temperature MIN: {[el for el in weather_days.temperature_min]} °C\n'
          f'Weather code: {[el for el in weather_days.weather_code]}°\n'
          f'Date: {[el for el in weather_days.time]}\n')