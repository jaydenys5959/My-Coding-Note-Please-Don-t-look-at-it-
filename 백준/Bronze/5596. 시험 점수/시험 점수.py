ans_S = 0
ans_T = 0 
S = map(int,input().split())
T = map(int,input().split())
ans_T = sum(T)
ans_S = sum(S)
if ans_T > ans_S:
    print(ans_T)
else:
    print(ans_S)
    
