# DailyResponse

For each selected daily weather variable, data will be returned as a floating point array. Additionally a `time` array will be returned with ISO8601 timestamps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **List[str]** |  | 
**temperature_2m_max** | **List[float]** |  | [optional] 
**temperature_2m_min** | **List[float]** |  | [optional] 
**apparent_temperature_max** | **List[float]** |  | [optional] 
**apparent_temperature_min** | **List[float]** |  | [optional] 
**precipitation_sum** | **List[float]** |  | [optional] 
**precipitation_hours** | **List[float]** |  | [optional] 
**weather_code** | **List[float]** |  | [optional] 
**sunrise** | **List[float]** |  | [optional] 
**sunset** | **List[float]** |  | [optional] 
**wind_speed_10m_max** | **List[float]** |  | [optional] 
**wind_gusts_10m_max** | **List[float]** |  | [optional] 
**wind_direction_10m_dominant** | **List[float]** |  | [optional] 
**shortwave_radiation_sum** | **List[float]** |  | [optional] 
**uv_index_max** | **List[float]** |  | [optional] 
**uv_index_clear_sky_max** | **List[float]** |  | [optional] 
**et0_fao_evapotranspiration** | **List[float]** |  | [optional] 

## Example

```python
from weather.models.daily_response import DailyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DailyResponse from a JSON string
daily_response_instance = DailyResponse.from_json(json)
# print the JSON string representation of the object
print(DailyResponse.to_json())

# convert the object into a dict
daily_response_dict = daily_response_instance.to_dict()
# create an instance of DailyResponse from a dict
daily_response_from_dict = DailyResponse.from_dict(daily_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


