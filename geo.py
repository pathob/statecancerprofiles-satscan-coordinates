import csv
import sys
import os.path
from geopy.geocoders import Nominatim

print(str(sys.argv))

# exit program if no file is specified
if len(sys.argv) != 2:
    print("Please specify a file")
    sys.exit()

casefile = sys.argv[1]

if not os.path.isfile(casefile):
    print("File " + casefile + " not found")
    sys.exit()

# init objects
geolocator = Nominatim()
locations = set()

# save existing geolocations to set
if os.path.isfile('geo.csv'):
    with open('geo.csv', newline='') as geofile:
        georeader = csv.reader(geofile, delimiter=';')

        for georow in georeader:
            location = georow[0]
            locations.add(location)

notfound = set()

# find non-existing geolocations in the internet
with open(str(casefile), newline='') as casesfile:
    with open('geo.csv', 'a', newline='') as geofile:
        casereader = csv.reader(casesfile, delimiter=';')
        geowriter = csv.writer(geofile, delimiter=';')

        for caserow in casereader:
            location = caserow[0]

            if location not in locations:
                try:
                    locationgeo = geolocator.geocode("USA " + location)
                
                    if hasattr(locationgeo, 'latitude') and hasattr(locationgeo, 'longitude'):
                        locations.add(location)
                        print((location, locationgeo.latitude, locationgeo.longitude))
                        geowriter.writerow([location, locationgeo.latitude, locationgeo.longitude])

                    else:
                        notfound.add(location)

                except:
                    print("Too many requests sent, try again later")
                    break

if len(notfound) > 0:
    print("")
    print("Didn't found these locations online:")

    for location in notfound:
        print((location))
