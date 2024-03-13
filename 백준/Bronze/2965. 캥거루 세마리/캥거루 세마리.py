A,B,C = map(int,input().split())
S = C-B -1
W = B-A -1
if W >= S:
    print(W)
else:
    print(S)
