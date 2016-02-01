A = raw_input()
B = raw_input()
C = []
for i in range(len(A)):
    C.append(int(A[i]) - int(B[i]))

if A[i] == B[i]:
    C[i] = C[i]+1
else:
    C[i] = C[i]-1    

ans = int(''.join(map(str, C)))
print ans

