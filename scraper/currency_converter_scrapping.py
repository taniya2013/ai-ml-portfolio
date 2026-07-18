import requests

def currency_converter(from_currency, to_currency, amount):

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url)
    data = response.json()

    if data["result"] != "success":
        return None

    rate = data["rates"][to_currency]

    return {
        "From Currency": from_currency,
        "To Currency": to_currency,
        "Amount": amount,
        "Exchange Rate": rate,
        "Converted Amount": round(amount * rate, 2),
        "Last Updated": data["time_last_update_utc"]
    }