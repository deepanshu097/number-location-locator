import phonenumbers

import folium
from myNumber import number

from phonenumbers import geocoder

key = '30f81a032a8c4ca5a72ff1252a1bd741'

unknownNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(unknownNumber, 'en')
print(yourLocation)

# service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,'en'))

#locating on map

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)
results = geocoder.geocode(query)
##print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(Location=[lat,lng], zoom_start = 9)

folium.Marker([lat,lng],popup = yourLocation).add_to(myMap)

##saving map in html

myMap.save("myLocation.html")