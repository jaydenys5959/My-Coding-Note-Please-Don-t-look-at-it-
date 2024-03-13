A,B = map(int,input().split())
C,D = map(int,input().split())
ans = 0
S = B+C
U = A+D
if S <= U:
    ans = S
else:
    ans = U
print(ans)



    
    
