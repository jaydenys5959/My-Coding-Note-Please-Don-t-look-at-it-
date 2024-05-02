A = int(input())
W = 0
for i in range(A):
    s = int(input())
    n = int(input())
    W = s
    for z in range(n):
        q,p = map(int,input().split())
        W += q * p
    print(W)
        

