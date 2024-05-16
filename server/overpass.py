import overpy

api = overpy.Overpass()

# fetch all ways and nodes
#result = api.query("""[out:json];way["building"]["addr:city"="Kelkheim"]["addr:street"="Taunushöhe"]["addr:postcode"="65779"]["addr:country"="DE"]["addr:housenumber"="33"];>;out qt;""")
result = api.query("""[out:json];way["building"]["addr:city"="Berlin"]["addr:street"="Waldstraße"]["addr:housenumber"="1"];out qt;>; out qt;""")
#print(vars(result))
print(result.ways)

def request_location(city: str, postal_code: str, street: str, house_number: str):
    result = api.query(f"""[out:json];way["addr:city"="{city}"]["addr:street"="{street}"]["addr:housenumber"="{house_number}"]out;""")
    ways = result.ways
    nodes = result.nodes
    print(ways)
