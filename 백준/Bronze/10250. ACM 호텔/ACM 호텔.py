N = int(input())

for i in range(N):
    H,W,N = map(int,input().split())
    if N % H == 0:
        print(H * 100 + N // H)
    else:
        print((N%H * 100) + (N//H+1))