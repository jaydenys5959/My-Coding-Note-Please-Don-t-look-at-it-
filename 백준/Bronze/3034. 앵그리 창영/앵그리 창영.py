N,W,H = map(int,input().split())
check = ((W*W) + (H*H)) ** 0.5

for i in range(N):
    o = int(input())
    if o <= check:
        print("DA")
    else:
        print("NE")
        