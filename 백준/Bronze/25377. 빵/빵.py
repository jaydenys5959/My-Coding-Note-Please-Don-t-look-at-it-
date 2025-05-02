N = int(input())
min = 1001
for n in range(N):
    time,bread = map(int,input().split())
    if time <= bread:
        if bread < min:
            min = bread
if min == 1001:
    print(-1)
else:
    print(min)            