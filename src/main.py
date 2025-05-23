import inspect
import os
import sys
import logging

import weatherapi
from mcp.server.fastmcp import FastMCP


logger = logging.getLogger(__name__)


class WeatherSSEServer:
    """MCP Server that connects to OpenWeatherMap API through SSE."""

    def __init__(self, api_key: str, port: int = 8080, host: str = "0.0.0.0"):
        self.api_key = api_key
        self.port = port
        self.host = host
        configuration = weatherapi.Configuration()
        configuration.api_key["key"] = api_key
        self._weather_api = weatherapi.APIsApi(weatherapi.ApiClient(configuration))

        self.server = FastMCP("Weather SSE Server", version="1.0.0", host=host, port=port)

        self._register_tools()

    def start(self):
        logger.info(f"Starting MCP Weather SSE Server on {self.host}:{self.port}")
        self.server.run(transport="sse")

    def _register_tools(self):
        all_members = inspect.getmembers(self._weather_api, inspect.ismethod)
        filtered_members = [x for x in all_members if not x[0].startswith("_") and not x[0].endswith("_http_info")]
        for member in filtered_members:
            self.server.add_tool(
                name=member[0],
                fn=member[1],
                description=inspect.getdoc(filtered_members[0][1]),
            )


def main():
    api_key = os.environ.get("WEATHER_API_KEY")

    if not api_key:
        logger.error(
            "API key is required. Please provide it using --api-key or set the EATHER_API_KEY environment variable."
        )
        sys.exit(1)

    server = WeatherSSEServer(api_key=api_key)
    server.start()


if __name__ == "__main__":
    main()
