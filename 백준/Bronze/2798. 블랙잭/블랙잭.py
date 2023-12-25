A,B = map(int,input().split())
C = list(map(int,input().split()))
ans = 0
for i in range(A):
    for z in range(i+1,A):
        for f in range(z+1,A):
            AH = C[i] + C[z] + C[f]
            if AH <= B:
                if ans < AH:
                    ans = AH
print(ans)
