import googlemaps
import json
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDzEneQdlBYzQ5ubhoLprvwU9BFzxI5Eug')

def get_distance(origins, destinations, print_to_screen=True):
    """get distance between two or more places"""
    distance = gmaps.distance_matrix(
        origins=origins,
        destinations=destinations
    )
    if print_to_screen:
        print(json.dumps(distance, indent=4))
    return distance

def get_directions(origin, destination, print_to_screen=False):
    """Get directions to destination from origin"""
    directions = gmaps.directions(
        origin=origin,
        destination=destination,
        mode="driving",
        departure_time=datetime.now()
    )
    if print_to_screen:
        print(json.dumps(directions, indent=4))
    return directions

origin = input("Enter starting point: ").strip(".,- ")
print(origin)
destination = input("Enter delivering point: ").strip(".,- ")
print(destination)

check = 'y'
check = input("Do you wnat to know the distance between %s and %s ? (y/n)" % (origin, destination))
if check=='y':
    get_distance(origin, destination)

prnt_dir = 'n'
prnt_dir = input("Do you want to get directions from %s to %s? (y/n)" % (origin, destination))
if prnt_dir == 'y':
    get_directions(origin, destination, print_to_screen=True)
