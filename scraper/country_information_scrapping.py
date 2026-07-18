import requests

def get_country_information(country):

    url = "https://countriesnow.space/api/v0.1/countries"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    countries = response.json()["data"]

    for item in countries:
        if item["country"].lower() == country.lower():

            return {
                "Country": item["country"],
                "Cities": ", ".join(item["cities"][:15])
            }

    return None