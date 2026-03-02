"""Test module for MCP Weather Server."""

import os
from unittest.mock import MagicMock, patch

from main import WeatherSSEServer, main


class TestWeatherSSEServer:
    """Tests for WeatherSSEServer class."""

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    def test_init_default_transport(self, mock_fastmcp_class, mock_weather_api_class):
        """Test server initialization with default transport."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp

        server = WeatherSSEServer()

        assert server._port == 8080
        assert server._host == "0.0.0.0"
        assert server._transport == "streamable-http"
        mock_weather_api_class.assert_called_once()

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    def test_init_custom_transport(self, mock_fastmcp_class, mock_weather_api_class):
        """Test server initialization with custom transport."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp

        server = WeatherSSEServer(transport="sse")

        assert server._transport == "sse"
        mock_weather_api_class.assert_called_once()

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    def test_init_custom_host_and_port(
        self, mock_fastmcp_class, mock_weather_api_class
    ):
        """Test server initialization with custom host and port."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp

        server = WeatherSSEServer(host="127.0.0.1", port=3000)

        assert server._port == 3000
        assert server._host == "127.0.0.1"
        mock_weather_api_class.assert_called_once()

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    @patch("main.logger")
    def test_start_server(
        self, mock_logger, mock_fastmcp_class, mock_weather_api_class
    ):
        """Test server start method."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp
        server = WeatherSSEServer()

        with patch.object(server._server, "run"):
            server.start()

        mock_logger.info.assert_called_once_with(
            "Starting MCP Weather Server on 0.0.0.0:8080 using streamable-http"
        )

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    def test_register_tools(self, mock_fastmcp_class, mock_weather_api_class):
        """Test tool registration."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp

        server = WeatherSSEServer()

        assert server._server == mock_fastmcp
        assert server._client == mock_api
        mock_weather_api_class.assert_called_once()

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    def test_register_tools_filters_private_methods(
        self, mock_fastmcp_class, mock_weather_api_class
    ):
        """Test that private methods are filtered from tool registration."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp

        server = WeatherSSEServer()

        tools = server._server._tools
        for tool in tools:
            assert not tool.name.startswith("_")

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    @patch("main.logger")
    def test_main_with_valid_transports(
        self, mock_logger, mock_fastmcp_class, mock_weather_api_class
    ):
        """Test main function with valid transports."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp

        with (
            patch("main.WeatherSSEServer.start"),
            patch.dict(
                os.environ,
                {"TRANSPORT": "streamable-http", "PORT": "8080", "HOST": "0.0.0.0"},
            ),
        ):
            main()

        mock_weather_api_class.assert_called_once()

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    @patch("main.logger")
    @patch("builtins.exit")
    def test_main_invalid_transport(
        self, mock_exit, mock_logger, mock_fastmcp_class, mock_weather_api_class
    ):
        """Test main function with invalid transport."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp

        with patch.dict(
            os.environ, {"TRANSPORT": "invalid", "PORT": "8080", "HOST": "0.0.0.0"}
        ):
            main()

        mock_exit.assert_called_once()
        mock_logger.fatal.assert_called_once()
        assert "not recognized" in mock_logger.fatal.call_args[0][0]

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    @patch("main.logger")
    @patch("builtins.exit")
    def test_main_custom_configuration(
        self, mock_exit, mock_logger, mock_fastmcp_class, mock_weather_api_class
    ):
        """Test main function with custom configuration."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp

        with (
            patch("main.WeatherSSEServer.start"),
            patch.dict(
                os.environ, {"TRANSPORT": "sse", "PORT": "9090", "HOST": "192.168.1.1"}
            ),
        ):
            main()

        mock_weather_api_class.assert_called_once()

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    def test_server_attributes(self, mock_fastmcp_class, mock_weather_api_class):
        """Test server attributes are correctly set."""
        mock_api = MagicMock()
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp
        mock_weather_api_class.return_value = mock_api

        server = WeatherSSEServer()

        assert server._client == mock_api
        assert server._server == mock_fastmcp

    @patch("main.WeatherAPI")
    @patch("main.FastMCP")
    @patch("main.logger")
    def test_start_logging_message(
        self, mock_logger, mock_fastmcp_class, mock_weather_api_class
    ):
        """Test that start method logs appropriate message."""
        mock_api = MagicMock()
        mock_weather_api_class.return_value = mock_api
        mock_fastmcp = MagicMock()
        mock_fastmcp_class.return_value = mock_fastmcp
        server = WeatherSSEServer()

        with patch.object(server._server, "run"):
            server.start()

        expected_message = (
            "Starting MCP Weather Server on 0.0.0.0:8080 using streamable-http"
        )
        mock_logger.info.assert_any_call(expected_message)
