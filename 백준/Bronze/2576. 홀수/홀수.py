Q = 99
ans = 0
for i in range(7):
    N = int(input())
    A = N % 2
    if A == 1:
        if Q > N:
            Q = N 
        ans += N
if ans == 0 :
    print("-1")
else:
    print(ans)
    print(Q)
        
    
