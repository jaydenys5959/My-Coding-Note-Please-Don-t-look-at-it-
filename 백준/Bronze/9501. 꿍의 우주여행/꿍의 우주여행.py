T = int(input())
A = 0
B = 0
for i in range(T):
    ans = 0
    N,D = map(int,input().split())
    for j in range(N):
        V,F,C = map(int,input().split())
        A = F/C
        B = V * A
        if B >= D:
            ans += 1
    print(ans)