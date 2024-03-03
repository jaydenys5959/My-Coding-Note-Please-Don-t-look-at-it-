N = int(input())
A = list(map(int,input().split()))
M = 0 
Y = 0
for i in range(N):
    M += (A[i] // 60+1)* 15                  
    Y += (A[i] // 30+1) * 10
if M < Y:
    print("M",M)
elif Y < M:
	print("Y",Y)
else:
	print("Y","M",M)
    
