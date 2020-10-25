"""Testing web APIs with HTTP GET method"""

import json
import sys

import requests

def print_coord(city):
    """Retrieve city hall coordinates of the city from Open Street Map"""
    osm = "https://nominatim.openstreetmap.org/search"
    city = city + " Hotel de Ville"
    data = {'q': city, 'format': 'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    for item in json_list:
        display_name = item['display_name']
        short_name = display_name.split(", ")[0]
        lat = item['lat']
        lon = item['lon']
        street = display_name.split(", ")[1] + " " + display_name.split(", ")[2] + " " + display_name.split(", ")[3] + " " + display_name.split(", ")[4] + " " + display_name.split(", ")[5] + " " + display_name.split(", ")[6]
        print(f"{short_name}, {street} ({lat} - {lon})")

if __name__ == "__main__":
    try:
        service = sys.argv[1]
        if service == "cityHall":
            try:
                city = sys.argv[2]
                print_coord(city)
            except IndexError:
                print("Please enter the name of a city")
        else:
            print("Unknown action, please use either 'cityHall'")
    except IndexError:
        print("Missing action, please use either 'cityHall'")