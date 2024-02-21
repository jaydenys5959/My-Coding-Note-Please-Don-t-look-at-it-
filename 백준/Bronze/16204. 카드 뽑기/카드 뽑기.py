N,M,K = map(int,input().split())
front_O = M
back_O = K
front_X = N-M
back_X = N-K
if front_O < back_O:
    ans_O = front_O
else:
    ans_O = back_O
if front_X < back_X:
    ans_X = front_X
else:
    ans_X = back_X
print(ans_X + ans_O)