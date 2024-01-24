N,M,K = map(int,input().split())
A = 0
while N > 1 and M >= 1 and N + M >= K+3:
    N -= 2
    M -= 1 
    A += 1
print(A)
    
