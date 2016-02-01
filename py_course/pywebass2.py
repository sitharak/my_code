import re
file = open('regex_sum_214803.txt')
sum = 0
filtered = filter(lambda x: not re.match(r'^\s*$', x), file)
for line in filtered:
    line = line.rstrip()
    for word in line:
        ans = re.findall('[0-9]+',line)
    for i in ans:
        num = int(i)
        sum += num

print sum