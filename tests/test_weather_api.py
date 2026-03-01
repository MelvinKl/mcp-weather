import unittest
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from weather_api import WeatherAPI


class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.api = WeatherAPI()

    @patch("weather_api.requests.get")
    def test_get_weather(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"current_weather": {"temperature": 20}}
        mock_get.return_value = mock_response

        result = self.api.get_weather(latitude=52.52, longitude=13.405)

        mock_get.assert_called_once()
        self.assertEqual(result, {"current_weather": {"temperature": 20}})

    @patch("weather_api.requests.get")
    def test_get_weather_with_params(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"current_weather": {"temperature": 15}}
        mock_get.return_value = mock_response

        result = self.api.get_weather(latitude=40.7128, longitude=-74.0060)

        call_args = mock_get.call_args
        self.assertEqual(call_args[1]["params"]["latitude"], 40.7128)
        self.assertEqual(call_args[1]["params"]["longitude"], -74.0060)
        self.assertEqual(result, {"current_weather": {"temperature": 15}})
