import csv

def openCSV(fileName):
    with open('addresses.csv') as infile:
        with open(fileName + '.csv') as outfile:
            reader = csv.DictReader(infile)
            for row in reader:
                print(row)

        #findLocate()
        #dwrite = csv.DictWriter(outfile)




def findLocate():
    from geopy.geocoders import GoogleV3
    geolocator = GoogleV3




fileName = raw_input("Enter new filename: ")
open(fileName + '.csv', 'w')
openCSV(fileName)
