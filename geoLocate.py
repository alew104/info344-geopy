import csv
import geopy

def openCSV(fileName):
    with open('addresses.csv', 'r') as infile:
        with open(fileName + '.csv', 'w') as outfile:
            reader = csv.DictReader(infile)
            fnames = reader.fieldnames + ['latitude', 'longitude', 'county']
            print(fnames)
            write = csv.DictWriter(outfile, fieldnames = fnames)
            write.writeheader()
            print('wrote header')
            for row in reader:
                address = row['address']
                city = row['city']
                state = row['state']
                zipcode = row['zip']
                fullAddress = address + ' ' + city + ' ' + state + ' ' + zipcode
                from geopy.geocoders import Bing
                geocoder = Bing(api_key = 'AiLKeLoEcoIYjSYqbfCmHPTzpMa2m_UWqGuNehGs-Kf6xRKo3Yl0t4HKm2CEAcrA')
                loc = geocoder.geocode(fullAddress)
                county = loc.raw['address']['adminDistrict2']
                lat = loc.latitude
                lng = loc.longitude
                write.writerow({'address' : address,
                                'city' : city,
                                'state' : state,
                                'zip' : zipcode,
                                'latitude' : lat,
                                'longitude' : lng,
                                'county' : county
                                })








fileName = raw_input("Enter new filename: ")
open(fileName + '.csv', 'w')
openCSV(fileName)
print('finished, check file')
