# CurrentWeather

Current weather conditions with the attributes: time, temperature, wind_speed, wind_direction and weather_code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | 
**temperature** | **float** |  | 
**wind_speed** | **float** |  | 
**wind_direction** | **float** |  | 
**weather_code** | **int** |  | 

## Example

```python
from weather.models.current_weather import CurrentWeather

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentWeather from a JSON string
current_weather_instance = CurrentWeather.from_json(json)
# print the JSON string representation of the object
print(CurrentWeather.to_json())

# convert the object into a dict
current_weather_dict = current_weather_instance.to_dict()
# create an instance of CurrentWeather from a dict
current_weather_from_dict = CurrentWeather.from_dict(current_weather_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


