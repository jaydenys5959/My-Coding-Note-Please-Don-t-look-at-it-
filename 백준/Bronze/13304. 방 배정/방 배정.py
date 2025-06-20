N, K = map(int, input().split())
FS =  0 #1,2학년
TFM = 0 #3,4 M학년
TFF = 0 #3,4 F학년
FSM = 0 #5,6 M학년
FSF = 0 #5,6 F학년
ans = 0
for _ in range(N):
    Y, G = map(int, input().split())
    if Y == 0:
        if G == 3 or G == 4:
            TFF += 1
        elif G == 1 or G == 2:
            FS += 1
        else:
            FSF += 1
    elif Y == 1:
        if G == 3 or G == 4:
            TFM += 1
        elif G == 1 or G == 2:
            FS += 1
        else:
            FSM += 1
Q = [FS,TFM,TFF,FSM,FSF]
for p in Q:
    B = p//K
    C = p%K
    ans += B
    if C >= 1:
        ans += 1
print(ans)
            
            
        
