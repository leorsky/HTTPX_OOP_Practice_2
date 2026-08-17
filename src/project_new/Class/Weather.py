from dataclasses import dataclass


@dataclass
class Weather:
    temperature: float
    wind_speed: float
    wind_direction: int
    weather_code: int