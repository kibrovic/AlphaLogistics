import googlemaps
from pprint import pprint

gmaps = googlemaps.Client(key='AIzaSyDzEneQdlBYzQ5ubhoLprvwU9BFzxI5Eug')

def get_geocode(lat, lng):
    geocode = gmaps.reverse_geocode((lat +"," + lng), result_type="country")
    pprint(geocode)

get_geocode('45.815', '15.981')