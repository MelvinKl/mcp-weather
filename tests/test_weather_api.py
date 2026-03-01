import pytest
from unittest.mock import Mock, patch
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.weather_api import WeatherAPI


@pytest.fixture
def weather_api():
    return WeatherAPI()


def test_weather_api_initialization(weather_api):
    assert weather_api._base_url == "https://api.open-meteo.com/v1"


@patch("src.weather_api.requests.get")
def test_get_weather(mock_get, weather_api):
    mock_response = Mock()
    mock_response.json.return_value = {"current_weather": {"temperature": 20}}
    mock_get.return_value = mock_response

    result = weather_api.get_weather(latitude=52.52, longitude=13.41)

    mock_get.assert_called_once()
    assert result == {"current_weather": {"temperature": 20}}
