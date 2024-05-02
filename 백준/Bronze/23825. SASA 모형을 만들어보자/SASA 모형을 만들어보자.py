N,M = map(int,input().split())
A = N//2
B = M//2
ans = 0
if A >= B:
    ans += B
elif A <= B:
    ans += A
print(ans)