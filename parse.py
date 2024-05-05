import json

def get_coordinates_from_address(geojson_file, address):
    with open(geojson_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for feature in data['features']:
        properties = feature.get('properties', {})
        feature_address = properties.get('addr:street', '') + ' ' + properties.get('addr:housenumber', '')
        print("Address in GeoJSON:", feature_address)  # Print the address found in GeoJSON
        if feature_address.lower() == address.lower():
            geometry = feature.get('geometry', {})
            if geometry['type'] == 'Polygon':
                return geometry['coordinates'][0]  # Assuming the first set of coordinates represents the building

    # Return None if address not found
    return None

# Example usage:
geojson_file = 'export.geojson'
address = 'Wenckstraße 23'
coordinates = get_coordinates_from_address(geojson_file, address)
if coordinates:
    print("Coordinates for", address, "are:", coordinates)
else:
    print("Address", address, "not found in the GeoJSON file.")
