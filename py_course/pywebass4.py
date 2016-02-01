import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum = 0

tags = soup('span')
for tag in tags:
    num = tag.contents[0]
    num = int(num)
    sum += num
print sum
    
