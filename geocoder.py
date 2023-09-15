#!/usr/bin/python3

#!pip install geopy

import pandas as pd
df = pd.read_csv('llcc.tsv', delimiter='\t')
#print(df.head(1))

from geopy.geocoders import Nominatim
def get_lat_long(location_name):
    print(type(location_name), location_name)
    location_name = location_name + " , Argentina"
    print(location_name)
    geolocator = Nominatim(user_agent="my_geocoder")
    try:
        location = geolocator.geocode(location_name)
    except:
        return None, None, None
    if location:
        print(location.latitude, location.longitude, location)
        return location.latitude, location.longitude, location
    else:
        return None, None, None

df['Latitude'], df['Longitude'], df['location'] = zip(*df['Localidad'].apply(get_lat_long))

df.to_csv('')