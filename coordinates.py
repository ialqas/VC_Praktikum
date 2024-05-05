import geopy.distance
from app import analyse
from exif import Image
from PIL import Image, ExifTags
from parse import get_coordinates_from_address

# Function to get the coordinates of the image
def imagecoordinates(path):
    img = Image.open(path)
    #changed getexif() method to without underscore
    exif_data = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    if 'GPSInfo' in exif_data:
        gps_info = exif_data['GPSInfo']
        lat = gps_info[2]
        lon = gps_info[4]
        lat_ref = gps_info[1]
        lon_ref = gps_info[3]
        lat = lat[0] + lat[1]/60 + lat[2]/3600
        lon = lon[0] + lon[1]/60 + lon[2]/3600
        if lat_ref == 'S':
            lat = -lat
        if lon_ref == 'W':
            lon = -lon
        return  float(lon), float(lat)
    else:
        return None
    
    
def calculateCoordinates(imageCoords, houseCoords):
    if len(houseCoords) < 2:
        return None
    
    firstClostes = (0,0)
    secondClosest = (0,0)
    
    for coords in houseCoords:
        if geopy.distance.geodesic(imageCoords, coords).meters < geopy.distance.geodesic(imageCoords, firstClostes).meters:
            firstClostes = coords

    for coords in houseCoords:
        if geopy.distance.geodesic(imageCoords, coords).meters < geopy.distance.geodesic(imageCoords, secondClosest).meters and coords != firstClostes:
            secondClosest = coords

    return firstClostes, secondClosest


## Run Part
coords_1 = (8.660541, 49.8798987)
coords_2 = (8.6607032, 49.8799153)
coords_3 = (8.6606764, 49.8800241)
coords_4 = (8.6605142, 49.8800075)
coords_5 = (8.660541, 49.8798987)

coordsHouse = coords_1, coords_2, coords_3, coords_4, coords_5

imageCoords = imagecoordinates('static/files/analyseFile.jpg')

wenckCoords = get_coordinates_from_address('export.geojson', 'Wenckstraße 23')

corner1, corner2 = calculateCoordinates(imageCoords, wenckCoords)


widthHouse = geopy.distance.geodesic(corner1, corner2).meters
print(widthHouse)