from urllib.request import urlopen
import json

url = "http://py4e-data.dr-chuck.net/comments_1168119.json"
data = urlopen(url).read()
info  = json.loads(data)
total = 0
for i in info['comments']:
    total = int(i["count"]) + total

print(total) 
    
