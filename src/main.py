import inspect
import logging

from fastmcp import FastMCP

from weather.api_client import ApiClient
from weather.api.weather_forecast_apis_api import WeatherForecastAPIsApi

logger = logging.getLogger(__name__)


class WeatherSSEServer:
    """MCP Server that connects to Open-Meteo API through SSE."""

    def __init__(self, port: int = 8080, host: str = "0.0.0.0"):
        self._port = port
        self._host = host
        self._client = WeatherForecastAPIsApi(ApiClient())

        self._server = FastMCP(name="Weather SSE Server")

        self._register_tools()

    def start(self):
        logger.info(f"Starting MCP Weather SSE Server on {self._host}:{self._port}")
        self._server.run(
            # transport="streamable-http",
            transport="sse",
            host=self._host,
            port=self._port,
            mount_path="/",
        )

    def _register_tools(self):
        all_members = inspect.getmembers(self._client, inspect.ismethod)
        filtered_members = [x for x in all_members if not x[0].startswith("_") and not x[0].endswith("_http_info")]
        for member in filtered_members:
            self._server.add_tool(
                name=member[0],
                fn=member[1],
                description=inspect.getdoc(filtered_members[0][1]),
            )


def main():
    server = WeatherSSEServer()
    server.start()


if __name__ == "__main__":
    main()
