import requests
import json
import overpy

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

def get_nearby_nodes(lat, lon):
    api = overpy.Overpass()
    print("IN NOMIN", lat, lon)
    result = api.query(f"""[out:json];node(around:35.0, {lat}, {lon});way(bn)->.wy;node._(w.wy);out;""")
    markers = []
    for node in result.nodes:
        marker = {}
        marker["geocode"] = [float(node.lat), float(node.lon)]
        markers.append(marker)
    return markers

#print(get_nearby_nodes(50.133174350000004, 8.442105654987682))


