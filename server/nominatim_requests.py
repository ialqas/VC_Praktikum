import requests
import json

def get_location_by_address(street, housenumber, postal_code, city,):
    url = f"https://nominatim.openstreetmap.org/search?street={street} {housenumber}&city={city}&postalcode={postal_code}&format=jsonv2"
    response = requests.get(url)
    json_data = json.loads(response.text)
    return (json_data[0]["lat"], json_data[0]["lon"])

