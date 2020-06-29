from math import sin, cos, sqrt, atan2, radians
from pprint import pprint
import json
from crud import create_location

from server import app
from model import connect_to_db
connect_to_db(app)

def distance_between(lat1, lon1, lat2, lon2):

    # -1.23501836322248, 43.16366490907967
    # -1.23501836322248, 43.16366490907967
    # -1.235517589375377, 43.16350255161524

    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# def camino_distance(lat, lon):
#     camino_lat = radians(43.16366490907967)
#     camino_lon = radians(-1.23501836322248)
#     return distance_between(lat, lon, camino_lat, camino_lon)
#
#     distance_from_last_point = distance(last, us)
#     last_camino_distance = camino_distance(last)
#     total = last_camino_distance + distance_from_last_point

locations = {}
json_data = open('data/camino.json', 'r').read()
data = json.loads(json_data)

last_lat = radians(43.16366490907967)
last_lon = radians(-1.23501836322248)
distance = 0

for row in data:
    # lon = line[0]
    # lat = line[1]
    lat = float(row["lat"])
    lon = float(row["lon"])
    # lon, lat = line.strip().split(", ")

    # print(lat, lon)
# approximate radius of earth in km

    lat_r = radians(lat)
    lon_r = radians(lon)

    new_distance = distance_between(last_lat, last_lon, lat_r, lon_r)
    distance += new_distance

    # print("Result:", distance)
    locations[distance] = {"lat": lat, "lon": lon}
    create_location(lon, lat, distance)
    last_lat = lat_r
    last_lon = lon_r

# jsonify = json.dumps(locations)
# print(jsonify)
