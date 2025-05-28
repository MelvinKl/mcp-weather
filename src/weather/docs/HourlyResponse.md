# HourlyResponse

For each selected weather variable, data will be returned as a floating point array. Additionally a `time` array will be returned with ISO8601 timestamps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **List[str]** |  | 
**temperature_2m** | **List[float]** |  | [optional] 
**relative_humidity_2m** | **List[float]** |  | [optional] 
**dew_point_2m** | **List[float]** |  | [optional] 
**apparent_temperature** | **List[float]** |  | [optional] 
**pressure_msl** | **List[float]** |  | [optional] 
**cloud_cover** | **List[float]** |  | [optional] 
**cloud_cover_low** | **List[float]** |  | [optional] 
**cloud_cover_mid** | **List[float]** |  | [optional] 
**cloud_cover_high** | **List[float]** |  | [optional] 
**wind_speed_10m** | **List[float]** |  | [optional] 
**wind_speed_80m** | **List[float]** |  | [optional] 
**wind_speed_120m** | **List[float]** |  | [optional] 
**wind_speed_180m** | **List[float]** |  | [optional] 
**wind_direction_10m** | **List[float]** |  | [optional] 
**wind_direction_80m** | **List[float]** |  | [optional] 
**wind_direction_120m** | **List[float]** |  | [optional] 
**wind_direction_180m** | **List[float]** |  | [optional] 
**wind_gusts_10m** | **List[float]** |  | [optional] 
**shortwave_radiation** | **List[float]** |  | [optional] 
**direct_radiation** | **List[float]** |  | [optional] 
**direct_normal_irradiance** | **List[float]** |  | [optional] 
**diffuse_radiation** | **List[float]** |  | [optional] 
**vapour_pressure_deficit** | **List[float]** |  | [optional] 
**evapotranspiration** | **List[float]** |  | [optional] 
**precipitation** | **List[float]** |  | [optional] 
**weather_code** | **List[float]** |  | [optional] 
**snow_height** | **List[float]** |  | [optional] 
**freezing_level_height** | **List[float]** |  | [optional] 
**soil_temperature_0cm** | **List[float]** |  | [optional] 
**soil_temperature_6cm** | **List[float]** |  | [optional] 
**soil_temperature_18cm** | **List[float]** |  | [optional] 
**soil_temperature_54cm** | **List[float]** |  | [optional] 
**soil_moisture_0_1cm** | **List[float]** |  | [optional] 
**soil_moisture_1_3cm** | **List[float]** |  | [optional] 
**soil_moisture_3_9cm** | **List[float]** |  | [optional] 
**soil_moisture_9_27cm** | **List[float]** |  | [optional] 
**soil_moisture_27_81cm** | **List[float]** |  | [optional] 

## Example

```python
from weather.models.hourly_response import HourlyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HourlyResponse from a JSON string
hourly_response_instance = HourlyResponse.from_json(json)
# print the JSON string representation of the object
print(HourlyResponse.to_json())

# convert the object into a dict
hourly_response_dict = hourly_response_instance.to_dict()
# create an instance of HourlyResponse from a dict
hourly_response_from_dict = HourlyResponse.from_dict(hourly_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


