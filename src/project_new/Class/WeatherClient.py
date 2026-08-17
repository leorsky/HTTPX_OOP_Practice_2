class WeatherClient:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_current_weather(self, latitude, longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "wind_speed_10m",
                "wind_direction_10m",
                "weather_code"
            ]
        }

        data = self.api_client.get(f'/v1/forecast', params=params)
        temperature = data['current']['temperature_2m']
        wind_speed = data['current']['wind_speed_10m']
        wind_direction = data['current']['wind_direction_10m']
        weather_code = data['current']['weather_code']
        return temperature, wind_speed, wind_direction, weather_code


    def get_forecast(self, latitude, longitude, days=3):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": "temperature_2m_max,temperature_2m_min,weather_code",
            "forecast_days": days
        }

        data = self.api_client.get(f'/v1/forecast', params=params)
        temperature_max = data['daily']['temperature_2m_max']
        temperature_min = data['daily']['temperature_2m_min']
        weather_code = data['daily']['weather_code']
        time_d = data['daily']['time']
        return temperature_max, temperature_min, weather_code, time_d