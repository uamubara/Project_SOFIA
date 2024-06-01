import os
import datetime

import pytz
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

base_url = 'https://api.openweathermap.org/data/2.5/weather'
# Replace "Weather_API_KEY" with your actual API key
api_key = os.environ.get('Weather_API_KEY')


def get_temperature(city):
    query = base_url + '?q=%s&units=imperial&APPID=%s' % (city, api_key)
    try:
        response = requests.get(query)
        if response.status_code != 200:
            return None  # Indicate weather data unavailable
        else:
            return response.json()
    except requests.exceptions.RequestException as error:
        print(error)
        return None  # Indicate an error occurred


def format_weather_data(weather_data):
    """
    This function formats the weather data into a natural language sentence,
    including wind speed converted to miles per hour (mph).
    """
    if weather_data:
        try:
            city_name = weather_data['name']
            temperature = int(weather_data['main']['temp'])
            feels_like = int(weather_data['main']['feels_like'])
            humidity = weather_data['main']['humidity']  # Percentage
            wind_speed = weather_data['wind']['speed']  # m/s (meters per second)

            # Convert wind speed from m/s to mph (multiply by conversion factor)
            wind_speed_mph = round(wind_speed * 2.237, 1)

            return f"{city_name} is currently experiencing {temperature} degrees Fahrenheit. It feels like {feels_like} degrees Fahrenheit with {humidity}% humidity and wind speeds of {wind_speed_mph} miles per hour."
        except KeyError:
            return "Error: Could not retrieve weather data."
    else:
        return "Weather data unavailable."


def get_local_time(timestamp, timezone_offset):
    """
    Converts a UTC timestamp to a local time string using the timezone offset in seconds.
    """
    utc_time = datetime.datetime.utcfromtimestamp(timestamp)
    local_time = utc_time + datetime.timedelta(seconds=timezone_offset)
    return local_time.strftime('%I:%M %p')


def get_sunrise_time(weather_data):
    """
    This function retrieves the sunrise time from the weather data
    and formats it into a human-readable format.
    """
    if weather_data:
        try:
            sunrise_timestamp = weather_data['sys']['sunrise']
            timezone_offset = weather_data['timezone']
            sunrise_time = get_local_time(sunrise_timestamp, timezone_offset)
            return f"Sunrise in {weather_data['name']} is at {sunrise_time}."
        except KeyError:
            return "Error: Could not retrieve sunrise time."
    else:
        return "Weather data unavailable."


def get_sunset_time(weather_data):
    """
    This function retrieves the sunset time from the weather data
    and formats it into a human-readable format.
    """
    if weather_data:
        try:
            sunset_timestamp = weather_data['sys']['sunset']
            timezone_offset = weather_data['timezone']
            sunset_time = get_local_time(sunset_timestamp, timezone_offset)
            return f"Sunset in {weather_data['name']} is at {sunset_time}."
        except KeyError:
            return "Error: Could not retrieve sunset time."
    else:
        return "Weather data unavailable."


def main():
    # Get user input (replace with Sofia's logic for retrieving city name)
    city_name = "new york"  # Replace with user-provided city or location

    weather_data = get_temperature(city_name)

    # Default weather information
    if weather_data:
        formatted_message = format_weather_data(weather_data)
        print(formatted_message)  # For testing purposes
    else:
        print("Weather data unavailable.")

    # Handle user requests for sunrise or sunset
    user_query = input("Do you want to know the sunrise or sunset time? (sunrise/sunset/both/no): ")

    if user_query.lower() == "sunrise":
        sunrise_message = get_sunrise_time(weather_data)
        print(sunrise_message)
    elif user_query.lower() == "sunset":
        sunset_message = get_sunset_time(weather_data)
        print(sunset_message)
    elif user_query.lower() == "both":
        sunrise_message = get_sunrise_time(weather_data)
        sunset_message = get_sunset_time(weather_data)
        print(sunrise_message)
        print(sunset_message)


if __name__ == '__main__':
    main()
