import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location : ')
xml = urllib.urlopen(url).read()
tree = ET.fromstring(xml)
sum = 0
counts = tree.findall('comments/comment')
for value in counts:
    num = value.find('count').text
    num = int(num)
    sum += num
print sum