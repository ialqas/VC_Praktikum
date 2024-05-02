import geopy.distance

coords_1 = (8.660541,
              49.8798987)
coords_2 = (8.6607032,
              49.8799153)

print(geopy.distance.geodesic(coords_1, coords_2).meters)

