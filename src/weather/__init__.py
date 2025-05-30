# coding: utf-8

# flake8: noqa

"""
Open-Meteo APIs

Open-Meteo offers free weather forecast APIs for open-source developers and non-commercial use. No API key is required.

The version of the OpenAPI document: 1.0
Contact: info@open-meteo.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from weather.api.weather_forecast_apis_api import WeatherForecastAPIsApi

# import ApiClient
from weather.api_response import ApiResponse
from weather.api_client import ApiClient
from weather.configuration import Configuration
from weather.exceptions import OpenApiException
from weather.exceptions import ApiTypeError
from weather.exceptions import ApiValueError
from weather.exceptions import ApiKeyError
from weather.exceptions import ApiAttributeError
from weather.exceptions import ApiException

# import models into sdk package
from weather.models.current_weather import CurrentWeather
from weather.models.daily_response import DailyResponse
from weather.models.hourly_response import HourlyResponse
from weather.models.v1_forecast_get200_response import V1ForecastGet200Response
from weather.models.v1_forecast_get400_response import V1ForecastGet400Response
