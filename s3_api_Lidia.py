"""Testing web APIs with HTTP GET method"""

import json
import sys

import requests

def print_coord(address):
    """Retrieve coordinates from Open Street Map"""
    osm = "https://nominatim.openstreetmap.org/search"
    data = {'q': address, 'format': 'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    for item in json_list:
        display_name = item['display_name']
        short_name = display_name.split(", ")[0]
        lat = item['lat']
        lon = item['lon']
        print(f"{short_name} ({lat} - {lon})")

if __name__ == "__main__":
    try:
        service = sys.argv[1]
        if service == "coord":
            try:
                address = sys.argv[2]
                print_coord(address)
            except IndexError:
                print("Please enter an address")
        elif service == "info":
            try:
                country_name = sys.argv[2]
                print_info(country_name)
            except IndexError:
                print("Please enter a country name")
        else:
            print("Unknown action, please use either 'coord' or 'info'")
    except IndexError:
        print("Missing action, please use either 'coord' or 'info'")
