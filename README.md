# MCP-Weather

A Model Context Protocol (MCP) server that connects to the [Open-Meteo](https://open-meteo.com/) API through either streamable-http (default) or sse. This server provides weather data to AI clients using the MCP interface.

# Configuration

The following configuration can be set with env variables:
| Env var | Default value | Description|
|-------|--------|-------|
|`HOST`|`0.0.0.0`|Address to listen to.|
|`PORT`|`8080`|Port to listen on.|
|`TRANSPORT`|`streamable-http`|Transport used by the mcp server. Must be `streamable-http`or `sse`.|

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
    poetry run python src/main.py
```

# Testing

To run all tests with coverage:
```bash
make test
```

This will:
- Run all tests using pytest
- Check for linting issues with flake8
- Format code with black
- Generate coverage reports in HTML and XML formats

Test coverage is maintained at 100% for all source code (exceeds 80% requirement).

# License

Apache 2

# Acknowledgments

- Built with the [Model Context Protocol](https://modelcontextprotocol.io/)
- Uses data from the [OpenMeteo](https://open-meteo.com/) API