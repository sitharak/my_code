import urllib
import json
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
 
address = raw_input('Enter location : ') 
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
data = urllib.urlopen(url).read()

js = json.loads(data)

loc = js["results"][0]["place_id"]
print loc