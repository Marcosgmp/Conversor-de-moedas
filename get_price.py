import requests

def get_price(crr_source, crr_target):
    link = f"https://economia.awesomeapi.com.br/last/{crr_source}-{crr_target}"
    req = requests.get(link)
    price = req.json()[f"{crr_source}{crr_target}"]["bid"]
    return price
