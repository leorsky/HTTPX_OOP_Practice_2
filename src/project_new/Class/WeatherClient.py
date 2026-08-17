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