import requests
import ollama

def get_weather_summary(city = "New York", api_key = <weather_api_key_goes_here>):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    url = f"{BASE_URL}?q={city}&appid={weather_api_key_goes_here}"
    
    # Making the API call
    response = requests.get(url).json()
    
    # Extracting data from the response
    temp_kelvin = response['main']['temp']
    temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
    weather_description = response['weather'][0]['description']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
    
    # Formatting the summary
    summary = (f"Current weather in {city}:\n"
               f"Temperature: {temp_fahrenheit:.2f}°F\n"
               f"Condition: {weather_description}\n"
               f"Humidity: {humidity}%\n"
               f"Wind Speed: {wind_speed}m/s")
    
    return summary


def get_chat_response(prompt_message, summary):
    stream = ollama.chat(
        model='mistral',
        messages=[{
            "role": 'user',
            'content': "You are a Weather Assistant, you must only reply in short sentences and in a conversational tone. Here is information about today's weather: " + summary + "Please use this information to answer the users' query: " + prompt_message
        }],
        stream=True,
    )

    response_content = ''  # Initialize an empty string to store the response
    for chunk in stream:
        response_content += chunk['message']['content']  # Append each chunk's content

    return response_content

# Example usage
#user_prompt = input('Prompt inside weather assistant: ')
#summary = get_weather_summary()
#response = get_chat_response(user_prompt, summary)
#print(response)  # You can print the response or do anything else with it
