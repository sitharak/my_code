T = raw_input()
input = []
for i in range(0,int(T)):
	input.append(int(raw_input()))
	


for number in input :
	if number%2 == 0:
		print number
	else:
		print number-1