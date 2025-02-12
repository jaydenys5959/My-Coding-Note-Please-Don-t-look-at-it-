N, K, P = map(int, input().split())
bread = [0] + list(map(int, input().split()))

ans = 0
for n in range(N):
    b = 0
    for k in range(1, K + 1):
        b += bread[n * K + k]
    if b > K - P:
        ans += 1
print(ans)