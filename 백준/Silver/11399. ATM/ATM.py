N = int(input())
P = list(map(int,input().split()))
P.sort()
count = 0
ans = 0
for i in range(N):
    count += P[i]
    ans += count
print(ans)

