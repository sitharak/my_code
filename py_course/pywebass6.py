import urllib
import json

url = raw_input('Enter url: ')
data = urllib.urlopen(url).read()
js = json.loads(data)
sum = 0
for item in js['comments']:
    cnt = item['count']
    sum += int(cnt)
print sum