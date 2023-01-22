from webex_bot.models.command import Command
import requests
import json

class WeatherByZIP(Command):
        def __init__(self) -> None:
                super().__init__(
                    command_keyboard="weather",
                    help_message="Get current weather by ZIP code",
                    card=None,
                )

        def execute(self, message, attachment_actions):
            OPENWEATHER_KEY= "4df3266b605555f5248107dd7082bc4a"

            zip_code = message.strip()

            url = "https://api.openweathermap.org/data/2.5/weather?"
            url += f"zip={zip_code}&units=metric&appid={OPENWEATHER_KEY}"

            response = requests.get(url)
            weather = response.json()

            city = weather['name']
            conditions = weather['weather'][0]['description']
            temperature = weather['main']['temp']
            humidity = weather['main']['humidity']
            wind = weather['wind']['speed']

            response_message = f"in {city}, it's currently {temperature}C° with {conditions}."
            response_message += f"Wind speed is {wind} km/h. Humidity is {humidity}%"

            return response_message