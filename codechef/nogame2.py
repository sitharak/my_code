import psyco
psyco.full()
T = raw_input()
input = []
for i in range(0,int(T)):
	input.append(int(raw_input()))

for number in input:
	i = number-1
	flag = 0
	while(i > 0):
		if (number<=1):
			break
		if(number%i) == 0:
			number = number - i
			flag = 1 if (flag == 0) else 0
			i = number - 1
		else:
			i = i-1
	print "ALICE" if(flag == 1) else "BOB"
	
		

	