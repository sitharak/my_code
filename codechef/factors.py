import sys
T = raw_input()

for i in range(int(T)):
    N = raw_input()
    lst = []
    hash = {}
    fact = 1
    lst = map(int,sys.stdin.readline().split())
    for no in lst:
        i = 2
        while i>1 and i<=no:
            if(no%i) == 0: 
                hash[i] = hash.get(i,0) + 1
                no /= i
                i = 2
                continue
            i += 1
    for (key,val) in hash.iteritems():
        fact = fact * (val+1)
    print fact
    
        
