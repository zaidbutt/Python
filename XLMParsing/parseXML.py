import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = " http://py4e-data.dr-chuck.net/comments_1168118.xml"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

tree = ET.fromstring(data)

results = tree.findall('.//count')

sums = 0
for i in results:
    sums = sums + int(i.text)

print(sums)