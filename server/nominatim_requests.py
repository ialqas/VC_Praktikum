import requests
import json

def get_location_by_address(street, housenumber, postal_code, city,):
    url = f"https://nominatim.openstreetmap.org/search?street={street} {housenumber}&city={city}&postalcode={postal_code}&format=jsonv2"
    headers = {
        "User-Agent": "TU Darmstadt Fraunhofer VC practical lesson 2024"
    }
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    if len(json_data) == 0:
        return ("x", "x")
    else:
        return (json_data[0]["lat"], json_data[0]["lon"])
    
#print(get_location_by_address("Hochschulstraße", "1", "64289", "Darmstadt"))

