n,T = map(int,input().split())
a = list(map(int,input().split()))
time = 0
ans = 0
for i in range(n):
    time += a[i]
    if time > T:
        break
    ans += 1
print(ans)
        
