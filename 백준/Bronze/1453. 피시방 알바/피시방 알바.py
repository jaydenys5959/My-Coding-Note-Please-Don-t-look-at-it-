ans = 0
com = [0] * 101
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    if com[A[i]] == 0:
        com[A[i]] = 1
    else:
        ans += 1
print(ans)
                      