from dataclasses import dataclass


@dataclass
class Weather:
    temperature: float
    wind_speed: float
    wind_direction: int
    weather_code: int


@dataclass
class WeatherDays:
    temperature_max: list
    temperature_min: list
    weather_code: list
    time: list