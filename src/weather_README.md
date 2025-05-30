# weather
Open-Meteo offers free weather forecast APIs for open-source developers and non-commercial use. No API key is required.

The `weather` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Generator version: 7.13.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://open-meteo.com](https://open-meteo.com)

## Requirements.

Python 3.9+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 2.1.0, < 3.0.0
* python-dateutil >= 2.8.2
* pydantic >= 2
* typing-extensions >= 4.7.1

## Getting Started

In your own code, to use this library to connect and interact with weather,
you can run the following:

```python

import weather
from weather.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = weather.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with weather.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weather.WeatherForecastAPIsApi(api_client)
    latitude = 3.4 # float | WGS84 coordinate
    longitude = 3.4 # float | WGS84 coordinate
    hourly = ['hourly_example'] # List[str] |  (optional)
    daily = ['daily_example'] # List[str] |  (optional)
    current_weather = True # bool |  (optional)
    temperature_unit = celsius # str |  (optional) (default to celsius)
    wind_speed_unit = kmh # str |  (optional) (default to kmh)
    timeformat = iso8601 # str | If format `unixtime` is selected, all time values are returned in UNIX epoch time in seconds. Please not that all time is then in GMT+0! For daily values with unix timestamp, please apply `utc_offset_seconds` again to get the correct date. (optional) (default to iso8601)
    timezone = 'timezone_example' # str | If `timezone` is set, all timestamps are returned as local-time and data is returned starting at 0:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported. (optional)
    past_days = 56 # int | If `past_days` is set, yesterdays or the day before yesterdays data are also returned. (optional)

    try:
        # 7 day weather forecast for coordinates
        api_response = api_instance.v1_forecast_get(latitude, longitude, hourly=hourly, daily=daily, current_weather=current_weather, temperature_unit=temperature_unit, wind_speed_unit=wind_speed_unit, timeformat=timeformat, timezone=timezone, past_days=past_days)
        print("The response of WeatherForecastAPIsApi->v1_forecast_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WeatherForecastAPIsApi->v1_forecast_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*WeatherForecastAPIsApi* | [**v1_forecast_get**](weather/docs/WeatherForecastAPIsApi.md#v1_forecast_get) | **GET** /v1/forecast | 7 day weather forecast for coordinates


## Documentation For Models

 - [CurrentWeather](weather/docs/CurrentWeather.md)
 - [DailyResponse](weather/docs/DailyResponse.md)
 - [HourlyResponse](weather/docs/HourlyResponse.md)
 - [V1ForecastGet200Response](weather/docs/V1ForecastGet200Response.md)
 - [V1ForecastGet400Response](weather/docs/V1ForecastGet400Response.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

info@open-meteo.com


