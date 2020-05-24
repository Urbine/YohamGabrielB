# First off, let's import the libraries we require to make the whole process

import urllib.parse, urllib.request, urllib.error
import json
import ssl

# I am ignoring any certificate errors with this
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Here I aim to obtain the data from the internet
url = input('Enter data location:')
hnd = urllib.request.urlopen(url, context=ctx).read()
data = json.loads(hnd)
print('Retrieving:', url)

# Here the variables are initialized to store the results of the computation
count = -1
countSum = 0

# Then I iterate through all the values possible by using an indefinite loop
while True:
    try:
        print(data["comments"][count]["count"])                      # We need to keep track of the indexes
        count = count + 1                                            # and add them as part of our expression
        countSum = countSum + int(data["comments"][count]["count"])  # also it's important to typecast our values
    except:
        break  # When it reaches the end, it will stop

print('The sum of all the count elements is:', countSum)             # I printed out the count (times) and the sum
print('We computed', count, 'elements in this JSON file')
