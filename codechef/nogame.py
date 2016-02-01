T = raw_input()
input = []
for i in range(0,int(T)):
	input.append(int(raw_input()))

flag = 0

for number in input:
	for i in range (number-1,0,-1):
		print "no at beg", number
		if (number<=1):
			break
		if(number%i) == 0:
			number = number - i
			print "no within middle", number
			global flag
			flag = 1 if (flag == 0) else 0
			print "flag", flag
		print "no at end", number
	if(flag == 0):
		print "ALICE"
	else:
		print "BOB"
		

	