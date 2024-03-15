# Weather Chat Assistant

## Description
This project integrates weather data fetching and conversational AI to create a Weather Chat Assistant. It uses the OpenWeatherMap API to get current weather conditions for any given city and formats this data into a concise summary. This summary is then fed into an ollama-based chat model to generate conversational responses to user queries about the weather.

## Requirements
- Python 3.x
- `requests` library
- `ollama` library
- An API key from OpenWeatherMap

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Install the required Python libraries using pip:
    ```
    pip install requests ollama
    ```
3. Sign up for an OpenWeatherMap API key and store it in a file named `weather_api_key.py` with the variable `api_data` containing your API key as a string.

## Usage

To use the Weather Chat Assistant, you need to run the provided Python script. It's structured to require minimal setup:

1. Ensure your OpenWeatherMap API key is correctly set up in `weather_api_key.py`.
2. Import the main functions from the script:
    ```python
    from <your_script_name> import get_weather_summary, get_chat_response
    ```
3. Get the weather summary by calling `get_weather_summary(city="CityName")`, replacing `"CityName"` with your desired city.
4. Use the summary to generate a conversational response to a weather-related query by calling `get_chat_response(prompt_message="YourQueryHere", summary=summary)`.

## Example
```python
# Fetch weather summary
summary = get_weather_summary(city="New York")

# Generate a conversational response to a query
response = get_chat_response(prompt_message="Will it rain today?", summary=summary)

print(response)  # Prints the conversational AI's response
