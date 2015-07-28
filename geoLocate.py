import csv

def openCSV(fileName):
    with open('addresses.csv') as infile:
        with open(fileName + '.csv') as outfile:
            reader = csv.DictReader(infile)
            fnames = reader.fieldnames + ['latitude', 'longitude', 'county']
            print(fnames)
            write = csv.DictWriter(outfile, fnames = fnames)
            write.writeheader(fnames)
            print('wrote header')
            for row in reader:
                address = row['address']
                city = row['city']
                state = row['state']
                zipcode = row['zip']
                fullAddress = address + ' ' + city + ' ' + state + ' ' + zipcode
                print(fullAddress)
                findLocate(fullAddress)

        #findLocate()
        #dwrite = csv.DictWriter(outfile)




def findLocate(fullAddress):
    from geopy.geocoders import Bing
    geolocator = Bing(api_key = 'AiLKeLoEcoIYjSYqbfCmHPTzpMa2m_UWqGuNehGs-Kf6xRKo3Yl0t4HKm2CEAcrA')
    loc = geocoder.geocode(fullAddress)
    print(loc.raw)




fileName = raw_input("Enter new filename: ")
open(fileName + '.csv', 'w')
openCSV(fileName)
