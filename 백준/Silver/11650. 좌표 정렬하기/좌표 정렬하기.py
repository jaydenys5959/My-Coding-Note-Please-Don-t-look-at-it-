N = int(input())
R = []
for i in range(N):
    X,Y = map(int,input().split())
    R.append([X,Y])
R.sort()
for i in range(N):
    print(R[i][0],R[i][1])
