# MCP-Weather

A Model Context Protocol (MCP) server that connects to the [Open-Meteo](https://open-meteo.com/) API through streamable-http. This server provides weather data to AI clients using the MCP interface.

# Requirements
It is recommended to use the provided Dockerimage, which requires only Docker to be installed.

If you want to install from source the following packages are required:
- Python 3.13
- Poetry

# Installation
## (Recommended) Using the Dockerimage
```bash
    docker run -p 8080:8080 ghcr.io/melvinkl/mcp-weather/server:latest
```
## Using source
1. Clone the repository
```bash
    git clone https://github.com/MelvinKl/mcp-weather.git
```
2. Install the dependencies
```bash
    poetry install --no-root
```
3. Runs the server
```bash
    poetry run pythonsrc/main.py
```

# License

Apache 2

# Acknowledgments

- Built with the [Model Context Protocol](https://modelcontextprotocol.io/)
- Uses data from the [OpenMeteo](https://open-meteo.com/) API