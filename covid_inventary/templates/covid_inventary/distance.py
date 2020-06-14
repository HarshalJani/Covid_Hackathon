from math import cos, asin, sqrt

#Haversine formula
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def closest(data, v):
    return min(data, key=lambda p: distance(v['lat'],v['lon'],p['lat'],p['lon']))

def fetch_id(base_dict, closest):

    for key, val in d.items():

        if float(val[0]['latitude']) == closest_cordinate['lat'] and float(val[0]['longitude']) == closest_cordinate['lon']:
            return val[0]['id']


def closest_cordinate(lat, longi, data):
	base_cordinate = {'lat': lat, 'lon': longi}
	cord_list = []
	for k,v in data.items():

    	new_lat = float(v[0]['seller_lat'])
    	new_long = float(v[0]['seller_long'])

    	cord_dict = {'lat' : new_lat, 'lon' : new_long}
    	cord_list.append(cord_dict)

    closest_cordinate = closest(cord_list, base_cordinate)
    closest_cordinate['id'] = fetch_id(d, closest_cordinate)
    print(closest_cordinate)
    return closest_cordinate

