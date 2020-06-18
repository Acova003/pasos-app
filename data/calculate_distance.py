from math import sin, cos, sqrt, atan2, radians

with open('output.py') as f:
    for line in f:
        # lon = line[0]
        # lat = line[1]
        lon, lat = line.strip().split(", ")
        print(lat, lon)
# approximate radius of earth in km
        R = 6373.0

        lat1 = radians(float(lat))
        lon1 = radians(float(lon))
        lat2 = radians(43.16366490907967)
        lon2 = radians(-1.23501836322248)
        # -1.23501836322248, 43.16366490907967
        # -1.23501836322248, 43.16366490907967
        # -1.235517589375377, 43.16350255161524

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        print("Result:", distance)
