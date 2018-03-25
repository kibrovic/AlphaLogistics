import googlemaps
import re
from pprint import pprint
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDzEneQdlBYzQ5ubhoLprvwU9BFzxI5Eug')

def get_distance(origins, destinations):
    """get distance between two or more places"""
    distance = gmaps.distance_matrix(
        origins=origins,
        destinations=destinations
    )
    return distance['rows'][0]['elements'][0]

def get_directions(origin, destination):
    """Get directions to destination from origin"""
    directions = gmaps.directions(
        origin=origin,
        destination=destination,
        mode="driving",
        departure_time=datetime.now()
    )
    return directions[0]['legs'][0]['steps']


def check_for_countries(directions_response):
    """Extract all countries entered"""
    print("checking for countries")
    countries = []
    coords = [i['end_location'] for i in directions_response]

    for i in range(len(coords)):
        print("checking %d geolocation" % i, end='\r')
        geocode = gmaps.reverse_geocode((str(coords[i]['lat']) + ',' + str(coords[i]['lng'])), result_type='country')
        countries.append(geocode[0]['address_components'][0]['long_name'])
    countries = list(set(countries))
    return(countries)

class RouteInfo:
    """Class to recieve directions object"""
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.distance = get_distance(self.origin, self.destination)['distance']['text']
        self.duration = get_distance(self.origin, self.destination)['duration']['text']
        self.directions = get_directions(self.origin, self.destination)
        self.countries = check_for_countries(self.directions)
        
    
def make_a_class(class_name, origin, destination):
    class_name = RouteInfo(origin, destination)
    return class_name


origin = input("Enter starting point: ").strip(".,- ")
print(origin)
destination = input("Enter delivering point: ").strip(".,- ")
print(destination)
new_name = origin + "_" + destination
new_name = make_a_class(new_name, origin, destination)

stop = 'n'
while stop != 'y':
    info = input("""
    What would you like to know: \n
    [1]: Origin \n
    [2]: Destination \n
    [3]: Distance \n
    [4]: Duration \n
    [5]: Directions \n
    [6]: Countries \n
    """)

    info_dir = {
        '1': new_name.origin,
        '2': new_name.destination,
        '3': new_name.distance,
        '4': new_name.duration,
        '5': new_name.directions,
        '6': new_name.countries
    }
    val = info_dir[info]
    pprint(val)

    stop = input("Do you want to stop? (y): ")
