"""Test module for WeatherAPI."""

from unittest.mock import MagicMock, patch

import pytest

from weather_api import WeatherAPI


class TestWeatherAPI:
    """Tests for WeatherAPI class."""

    @patch("weather_api.requests.get")
    def test_get_weather_success(self, mock_get):
        """Test successful weather data retrieval."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "current_weather": {"temperature": 20, "windspeed": 10},
            "daily": {
                "weather_code": [1],
                "temperature_2m_max": [25],
                "temperature_2m_min": [15],
            },
        }
        mock_get.return_value = mock_response

        api = WeatherAPI()
        result = api.get_weather(51.5, -0.1)

        assert isinstance(result, dict)
        assert "current_weather" in result
        assert "daily" in result

    @patch("weather_api.requests.get")
    def test_get_weather_invalid_coordinates(self, mock_get):
        """Test weather API with invalid coordinates."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Invalid coordinates"}
        mock_get.return_value = mock_response

        api = WeatherAPI()
        result = api.get_weather(999, 999)

        assert isinstance(result, dict)

    @patch("weather_api.requests.get")
    def test_get_weather_timeout(self, mock_get):
        """Test weather API timeout handling."""
        mock_get.side_effect = TimeoutError("Request timed out")

        api = WeatherAPI()
        with pytest.raises(TimeoutError):
            api.get_weather(51.5, -0.1)

    @patch("weather_api.requests.get")
    def test_get_weather_empty_response(self, mock_get):
        """Test weather API with empty response."""
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        api = WeatherAPI()
        result = api.get_weather(51.5, -0.1)

        assert isinstance(result, dict)
        assert result == {}

    @patch("weather_api.requests.get")
    def test_get_weather_with_all_daily_fields(self, mock_get):
        """Test weather API returns all required daily fields."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "current_weather": {"temperature": 20, "windspeed": 10},
            "daily": {
                "weather_code": [1],
                "temperature_2m_max": [25],
                "temperature_2m_min": [15],
                "apparent_temperature_max": [26],
                "apparent_temperature_min": [16],
                "sunrise": ["2023-01-01T08:00:00"],
                "sunset": ["2023-01-01T18:00:00"],
                "daylight_duration": [10],
                "sunshine_duration": [8],
                "uv_index_max": [5],
                "uv_index_clear_sky_max": [6],
                "rain_sum": [1],
                "showers_sum": [0.5],
                "precipitation_sum": [1.5],
                "snowfall_sum": [0],
                "precipitation_hours": [2],
                "precipitation_probability_max": [80],
                "wind_speed_10m_max": [20],
                "wind_gusts_10m_max": [25],
                "wind_direction_10m_dominant": [180],
                "shortwave_radiation_sum": [10],
                "et0_fao_evapotranspiration": [1],
                "relative_humidity_2m_min": [30],
                "relative_humidity_2m_max": [70],
                "relative_humidity_2m_mean": [50],
                "temperature_2m_mean": [20],
                "apparent_temperature_mean": [21],
                "cloud_cover_max": [90],
                "cloud_cover_min": [10],
                "cloud_cover_mean": [50],
                "dew_point_2m_mean": [10],
                "dew_point_2m_max": [15],
                "dew_point_2m_min": [5],
                "precipitation_probability_min": [20],
                "precipitation_probability_mean": [50],
                "surface_pressure_mean": [1013],
                "surface_pressure_max": [1015],
                "surface_pressure_min": [1011],
                "visibility_mean": [10],
                "visibility_min": [8],
                "visibility_max": [12],
            },
        }
        mock_get.return_value = mock_response

        api = WeatherAPI()
        result = api.get_weather(51.5, -0.1)

        assert isinstance(result, dict)
        assert "current_weather" in result
        assert "daily" in result

    def test_weather_api_initialization(self):
        """Test WeatherAPI initialization."""
        api = WeatherAPI()
        assert api._base_url == "https://api.open-meteo.com/v1"

    def test_weather_api_custom_base_url(self):
        """Test WeatherAPI with custom base URL."""
        api = WeatherAPI(base_url="https://custom.api.com/v1")
        assert api._base_url == "https://custom.api.com/v1"
