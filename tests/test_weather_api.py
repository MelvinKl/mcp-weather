import pytest
from unittest.mock import patch, MagicMock
from src.weather_api import WeatherAPI


@pytest.fixture
def weather_api():
    return WeatherAPI()


def test_weather_api_init(weather_api):
    assert weather_api._base_url == "https://api.open-meteo.com/v1"


def test_weather_api_init_custom_url():
    api = WeatherAPI(base_url="https://custom.api.com")
    assert api._base_url == "https://custom.api.com"


@patch("src.weather_api.requests.get")
def test_get_weather(mock_get, weather_api):
    mock_response = MagicMock()
    mock_response.json.return_value = {"current_weather": {"temperature": 20}}
    mock_get.return_value = mock_response

    result = weather_api.get_weather(latitude=52.52, longitude=13.41)

    mock_get.assert_called_once()
    assert result == {"current_weather": {"temperature": 20}}


@patch("src.weather_api.requests.get")
def test_get_weather_with_integer_coords(mock_get, weather_api):
    mock_response = MagicMock()
    mock_response.json.return_value = {"current_weather": {"temperature": 20}}
    mock_get.return_value = mock_response

    result = weather_api.get_weather(latitude=52, longitude=13)

    mock_get.assert_called_once()
    call_args = mock_get.call_args
    assert call_args[1]["params"]["latitude"] == 52
    assert call_args[1]["params"]["longitude"] == 13
    assert result == {"current_weather": {"temperature": 20}}
