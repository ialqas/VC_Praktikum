import geopy.distance
from typing import Tuple

def calculate_distance(coords_1: Tuple[int, int], coords_2: Tuple[int, int]) -> int:
    return geopy.distance.geodesic(coords_1, coords_2).meters