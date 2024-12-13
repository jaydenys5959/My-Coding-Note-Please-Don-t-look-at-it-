N = int(input())
R = []
for i in range(N):
    X,Y = map(int,input().split())
    R.append([Y,X])
R.sort()
for i in range(N):
    print(R[i][1],R[i][0])