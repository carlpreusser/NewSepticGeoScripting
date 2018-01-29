
from geopy.geocoders import Nominatim
import csv
import os
import time

geolocator = Nominatim()

csvF = os.path.abspath("C:\InstallerList.csv")

def do_geocode(address):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)

with open(csvF, "rt", encoding="utf8") as csvfile:
    with open('Output.csv', "a") as csvWriteFile:
        fReader = csv.reader(csvfile, delimiter=',', quotechar='"')
         
        for row in fReader:
            if (row[5] != "Address") and (row[5] != ""): 
                companyName = row[0]
                address = row[5] + " " + row[6] + " " + row[7] + " OH " + row[8]  

                location = do_geocode(address) 
                time.sleep(0.5)
                if location is not None:
                    lat = location.latitude
                    lon = location.longitude  
                    
                    strLat = str(lat)
                    strLon = str(lon)

                    line = companyName + ", " + address + ", " + strLat + ", " + strLon + "\n"

                    csvWriteFile.write(line)
                
