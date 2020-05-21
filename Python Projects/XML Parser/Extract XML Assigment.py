import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL Certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')             # Gathering input from the user
print('Retrieving', url)                   # Example location: http://py4e-data.dr-chuck.net/comments_265514.xml
print('Parsing...')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
count = 0                                  # Counts the elements
totalcounts = 0                            # Set initial sum value to zero
counts = tree.findall('comments/comment')  # Create list of comments
for item in counts:                        # Iterate through list
   x = item.find('count').text             # Pass count content to x
   totalcounts = totalcounts + int(x)      # Add integer of x to total
   count = count + 1
print('Count:', count)                     # Printing Count
print('Total Sum:', totalcounts)           # Printing element's sum (<count> tag).
