import requests

API_KEY = "09347103040aaebdd7d8da1b44bc26c4"


def weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        result = {
            "City": data["name"],
            "Country": data["sys"]["country"],
            "Temperature": f"{data['main']['temp']} °C",
            "Feels Like": f"{data['main']['feels_like']} °C",
            "Humidity": f"{data['main']['humidity']}%",
            "Weather": data["weather"][0]["main"],
            "Description": data["weather"][0]["description"],
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }

        return result

    return data   # Useful for seeing API errors


if __name__ == "__main__":
    city = input("Enter City: ")
    print(weather(city))