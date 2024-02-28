# README for Sports Betting Display Project

This project is designed to track and display sports betting odds in real-time. It uses WebSocket to receive betting data and aiohttp to display this data through a web interface.

## Features

- Subscribing to a stream of sports betting data via WebSocket.
- Processing and storing betting data in the server's memory.
- Displaying up-to-date betting data via an HTTP endpoint in JSON format.

## Installation and Running

Before starting, you need to have Python 3.7 or higher installed.

### Steps to install dependencies:

1. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Unix/Linux
    venv\Scripts\activate.bat # On Windows
    ```

2. Install the necessary dependencies:

    ```bash
    pip install websockets python-socks[asyncio] aiohttp orjson pympler
    ```

### Running the Server

Execute the following command to start the server:

```bash
python main.py
```