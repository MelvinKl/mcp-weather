# V1ForecastGet400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** | Always set true for errors | [optional] 
**reason** | **str** | Description of the error | [optional] 

## Example

```python
from weather.models.v1_forecast_get400_response import V1ForecastGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1ForecastGet400Response from a JSON string
v1_forecast_get400_response_instance = V1ForecastGet400Response.from_json(json)
# print the JSON string representation of the object
print(V1ForecastGet400Response.to_json())

# convert the object into a dict
v1_forecast_get400_response_dict = v1_forecast_get400_response_instance.to_dict()
# create an instance of V1ForecastGet400Response from a dict
v1_forecast_get400_response_from_dict = V1ForecastGet400Response.from_dict(v1_forecast_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


