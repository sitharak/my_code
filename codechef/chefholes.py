T = raw_input()
input = []
for i in range(0,int(T)):
	input.append(raw_input())
	
for string in input:	
	global cnt 
	cnt = 0
	for letter in string:
		if(letter == "A"or letter =="D"or letter =="O"or letter =="P"or letter =="Q"or letter =="R"):
			cnt = cnt+1
		elif(letter == 'B'):
			cnt = cnt+2
	print cnt

		
		
	
