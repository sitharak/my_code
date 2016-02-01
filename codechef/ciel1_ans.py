A, B = raw_input().split(" ")
C = int(A) - int(B)
posA = len(A)-1
posB = len(B)-1 
C = str(C)
posC = len(str(C))-1

if (A[posA] == B[posB]) or (C[posC] == '1'):
    no = int(C[posC])+1
else:
    no = int(C[posC])-1
    
C = C[:posC] + str(no)
print int(C)