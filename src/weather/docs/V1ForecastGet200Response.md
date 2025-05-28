# V1ForecastGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be up to 5 km away. | [optional] 
**longitude** | **float** | WGS84 of the center of the weather grid-cell which was used to generate this forecast. This coordinate might be up to 5 km away. | [optional] 
**elevation** | **float** | The elevation in meters of the selected weather grid-cell. In mountain terrain it might differ from the location you would expect. | [optional] 
**generationtime_ms** | **float** | Generation time of the weather forecast in milli seconds. This is mainly used for performance monitoring and improvements. | [optional] 
**utc_offset_seconds** | **int** | Applied timezone offset from the &amp;timezone&#x3D; parameter. | [optional] 
**hourly** | [**HourlyResponse**](HourlyResponse.md) |  | [optional] 
**hourly_units** | **Dict[str, str]** | For each selected weather variable, the unit will be listed here. | [optional] 
**daily** | [**DailyResponse**](DailyResponse.md) |  | [optional] 
**daily_units** | **Dict[str, str]** | For each selected daily weather variable, the unit will be listed here. | [optional] 
**current_weather** | [**CurrentWeather**](CurrentWeather.md) |  | [optional] 

## Example

```python
from weather.models.v1_forecast_get200_response import V1ForecastGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ForecastGet200Response from a JSON string
v1_forecast_get200_response_instance = V1ForecastGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1ForecastGet200Response.to_json())

# convert the object into a dict
v1_forecast_get200_response_dict = v1_forecast_get200_response_instance.to_dict()
# create an instance of V1ForecastGet200Response from a dict
v1_forecast_get200_response_from_dict = V1ForecastGet200Response.from_dict(v1_forecast_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


