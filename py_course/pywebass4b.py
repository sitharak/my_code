import urllib
from BeautifulSoup import *

url =  raw_input('Enter URL : ')
count = raw_input('Enter count : ')
pos = raw_input('Enter position : ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
count = int(count)
pos = int(pos)

while count > 0:
    tag = tags[pos-1]
    url = tag.get('href', None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    count  -= 1
    
print tag.text

    