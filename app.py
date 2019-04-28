import pandas

from geopy.geocoders import Nominatim

import geopy.geocoders

geopy.geocoders.options.default_user_agent = 'my_app/1'
geopy.geocoders.options.default_timeout = 7
geolocator = Nominatim()

df = pandas.read_json("supermarkets.json")

df["Address"]=df["Address"]+" ,"+df["City"]+" ,"+df["State"]+" ,"+df["Country"]

df["Coordinates"]=df["Address"].apply(geolocator.geocode)

df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude)

df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude)

df
