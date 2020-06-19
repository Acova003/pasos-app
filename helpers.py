from model import Location
import json

def get_location(distance_in):


    # to create locations
    #query to match distances less than distance traveled
    return Location.query.filter(Location.distance_in <= distance_in).order_by(Location.distance_in.desc()).first()

            # latitude = location['lat']
            # longitude = location['lon']

        # print(distance)
        #write sql query to get list of distance
    # geolocation = [latitude, longitude]
    # print(geolocation)
