import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input values for URL, Position, and Count to initiate the process.
url = input('Enter -')
position = int(input('Enter Position -'))
count = int(input('Enter Count -'))
# Global "for" loop to iterate using the count input as a range.
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# This will retrieve all of the <a> anchor tags to process to parse.
    tags = soup('a')
    final = list()  # Added them to a list in order to call out its indexes based on "position" input.

    for tag in tags:
        x = tag.get('href', None)
        final.append(x)

    print(final[position - 1])
    url = final[position - 1]  # This will modify the "URL" and follow it from the last coincidence in the parsing.

print("The answer is:", final[position - 1])
# As you may notice I added '-1' to position, that's why not all users know that Python indexes start in '0'.
