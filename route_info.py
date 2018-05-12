import googlemaps

from pprint import pprint
from datetime import datetime, timedelta

gmaps = googlemaps.Client(key='AIzaSyDzEneQdlBYzQ5ubhoLprvwU9BFzxI5Eug')

def get_distance(directions_response):
    """get distance between two or more places"""
    distance = [i['distance']['value'] for i in directions_response]
    return sum(distance)/1000

def get_duration(directions_response):
    """get time traveling between locations"""
    duration = [i['duration']['value'] for i in directions_response]
    return timedelta(seconds=sum(duration))


def get_directions(origin, destination, waypoints=None):
    """Get directions to destination from origin"""
    directions = gmaps.directions(
        origin,
        destination,
        waypoints=waypoints,
        mode="driving",
        departure_time=datetime.now()
    )
    return directions[0]['legs']


def check_for_countries(directions_response):
    """Extract all countries entered"""
    print("Prikupljanje geografskih podataka...")
    countries = []
    coords = [i['end_location'] for j in range(len(directions_response)) for i in directions_response[j]['steps']]

    for i in range(len(coords)):
        try:
            print("Provjera %d geolokacija" % i, end='\r')
            geocode = gmaps.reverse_geocode((str(coords[i]['lat']) + ',' + str(coords[i]['lng'])), result_type='country')
            countries.append(geocode[0]['address_components'][0]['long_name'])
        except IndentationError:
            print("IndentationError:")
            continue
        except IndexError:
            print("IndexError")
            continue
    countries = list(set(countries))
    return(countries)

class RouteInfo:
    """Class to recieve directions object"""
    def __init__(self, origin, destination, waypoints):
        self.origin = origin
        self.destination = destination
        self.waypoints = waypoints
        self.directions = get_directions(self.origin, self.destination, waypoints)
        self.distance = get_distance(self.directions)
        self.duration = get_duration(self.directions)
        self.countries = check_for_countries(self.directions)


def make_a_class(class_name, origin, destination, waypoints):
    class_name = RouteInfo(origin, destination, waypoints)
    return class_name

return_list = []
def get_route_info():
    origin = input("Unesite polazište: ").strip(".,- ")
    print(origin)
    destination = input("Unesite odredište: ").strip(".,- ")
    print(destination)
    waypoints = []
    stop = 'n'
    while stop !='y':
        waypoints.append(input("Usputna odredišta[prozivoljno]: "))
        stop = input("Stop (y/[n])")
    print('|'.join(waypoints))
    new_name = origin + "_" + destination
    new_name = make_a_class(new_name, origin, destination, waypoints)

    stop = 'n'
    while stop != 'y':
        info = input("""
        Dostupne informacije: \n
        [1]: Polazište \n
        [2]: Odredište \n
        [3]: Udaljenost \n
        [4]: Vrijeme vožnje \n
        [5]: Države\n
        """)

        info_dir = {
            '1': new_name.origin,
            '2': new_name.destination,
            '3': str(new_name.distance) + " (km)",
            '4': str(new_name.duration) + "(hh/mm/ss)",
            '5': "-".join(new_name.countries)
        }
        val = info_dir[info]
        print(val)

        stop = input("Stop (y/[n])")
    for val in info_dir.items():
        print(val[1])
        return_list.append(val[1])

    return return_list


#get_route_info()
