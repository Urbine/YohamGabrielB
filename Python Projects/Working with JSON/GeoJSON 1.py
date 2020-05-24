# First off, let's import the libraries we require to make the whole process
import urllib.parse, urllib.request, urllib.error
import json
import ssl

# serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?' (just in case that I want to add another API)
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')  # Example location: South Federal University
    apikey = 42                          # Another example location: University of Malaga
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'key': apikey, 'address': address})  # Address and API Key parameters
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)  # Load the JSON data the program obtained from outside
    except:
        js = None

    if not js or 'results' not in js or js['status'] != 'OK':  # Just in case I do not obtain the expected data.
        print('==== Failure To Retrieve ====')
        continue

    print(json.dumps(js, indent=4))  # Prints out the JSON Tree

    placeId = js["results"][0]["place_id"]  # The variable stores the JSON places I specified
    print("Place Id =", placeId)  # Prints out the Place ID of the university
    location = js['results'][0]['formatted_address']
    print(location)  # Along with the formatted address
