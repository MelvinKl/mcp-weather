# weather.WeatherForecastAPIsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_forecast_get**](WeatherForecastAPIsApi.md#v1_forecast_get) | **GET** /v1/forecast | 7 day weather forecast for coordinates


# **v1_forecast_get**
> V1ForecastGet200Response v1_forecast_get(latitude, longitude, hourly=hourly, daily=daily, current_weather=current_weather, temperature_unit=temperature_unit, wind_speed_unit=wind_speed_unit, timeformat=timeformat, timezone=timezone, past_days=past_days)

7 day weather forecast for coordinates

7 day weather variables in hourly and daily resolution for given WGS84 latitude and longitude coordinates. Available worldwide.

### Example


```python
import weather
from weather.models.v1_forecast_get200_response import V1ForecastGet200Response
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
    except Exception as e:
        print("Exception when calling WeatherForecastAPIsApi->v1_forecast_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| WGS84 coordinate | 
 **longitude** | **float**| WGS84 coordinate | 
 **hourly** | [**List[str]**](str.md)|  | [optional] 
 **daily** | [**List[str]**](str.md)|  | [optional] 
 **current_weather** | **bool**|  | [optional] 
 **temperature_unit** | **str**|  | [optional] [default to celsius]
 **wind_speed_unit** | **str**|  | [optional] [default to kmh]
 **timeformat** | **str**| If format &#x60;unixtime&#x60; is selected, all time values are returned in UNIX epoch time in seconds. Please not that all time is then in GMT+0! For daily values with unix timestamp, please apply &#x60;utc_offset_seconds&#x60; again to get the correct date. | [optional] [default to iso8601]
 **timezone** | **str**| If &#x60;timezone&#x60; is set, all timestamps are returned as local-time and data is returned starting at 0:00 local-time. Any time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) is supported. | [optional] 
 **past_days** | **int**| If &#x60;past_days&#x60; is set, yesterdays or the day before yesterdays data are also returned. | [optional] 

### Return type

[**V1ForecastGet200Response**](V1ForecastGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

