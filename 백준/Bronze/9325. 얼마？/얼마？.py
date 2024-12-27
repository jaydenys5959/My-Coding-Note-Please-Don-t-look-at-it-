A = int(input())
귀여미 = 0
for i in range(A):
    s = int(input())
    n = int(input())
    귀여미 = s
    for z in range(n):
        q,p = map(int,input().split())
        귀여미 += q * p
    print(귀여미)
        

