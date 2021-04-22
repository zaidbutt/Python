
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def retrieve(url):
    if len(names) == 7:
        print(names)
        exit()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = 1
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
    #print(tag.get('href', None))
        if count == 18:
            names.append(tag.contents[0])
            print("Retrieving Data From: ", tag.get("href", None))
            retrieve(tag.get('href', None))
        else:
            count = count + 1



url = input("URL: ")
names = []
retrieve(url)



        

