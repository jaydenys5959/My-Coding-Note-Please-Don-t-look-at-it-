A,B,C,D = map(int,input().split())
Z = A+D
W = B+C
if Z < W:
    P = W - Z
else:
    P = Z - W
print(P)
