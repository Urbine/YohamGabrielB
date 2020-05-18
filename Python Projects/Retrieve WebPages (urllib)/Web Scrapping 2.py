# Imported urllib and BeautifulSoup4 (from folder in the project files), and ssl.
import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location -')                  # Example locations: http://py4e-data.dr-chuck.net/comments_42.html
                                                 # http://py4e-data.dr-chuck.net/comments_265512.html

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')                               # Get the <span> tags
total = 0                                         # Set variable to '0'
for tag in tags:
    total = total + int(tag.contents[0])          # Extract content and add it to the variable.

print('The answer is:', total)                    # Print 'total' variable as the sum of the <span> tag contents.
