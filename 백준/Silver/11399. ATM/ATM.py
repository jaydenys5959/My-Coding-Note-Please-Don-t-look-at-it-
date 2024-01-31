N = int(input())
T = list(map(int,input().split()))
T.sort()
뚱이 = 0
똥이 = 0
for i in range(N):
    뚱이 += T[i]
    똥이 += 뚱이
print(똥이)
    