S1,S2,S3 = map(int,input().split())
ans = 0
count = [0] * 81
for i in range(S1) :  
    for j in range(S2) : 
        for z in range(S3) :
            A = i+j+z+3
            count[A] += 1
for i in range(1,81):
    if count[i] > count[ans]:
        ans = i
print(ans)

