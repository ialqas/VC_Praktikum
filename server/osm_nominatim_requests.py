import requests
import json
import overpy
from typing import Tuple, List, Dict

def get_location_by_address(street: str, housenumber: str, postal_code: str) -> Tuple[str, str]:
    url = f"https://nominatim.openstreetmap.org/search?street={street} {housenumber}&postalcode={postal_code}&format=jsonv2"
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

def get_nearby_nodes(lat: str, lon: str) -> List[Dict[str, List[float]]]:
    api = overpy.Overpass()
    result = api.query(f"""[out:json];node(around:75.0, {lat}, {lon});way(bn)->.wy;node._(w.wy);out;""")
    markers = []
    for node in result.nodes:
        marker = {}
        marker["geocode"] = [float(node.lat), float(node.lon)]
        markers.append(marker)
    return markers

#print(get_nearby_nodes(50.133174350000004, 8.442105654987682))


