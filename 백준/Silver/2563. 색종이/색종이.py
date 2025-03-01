N = int(input())
white = [[0] * 100 for i in range(100)]
for i in range(N):
    x,y = map(int,input().split())
    for r in range(y,y+10):
        for c in range(x,x+10):
            white[r][c] = 1
score = 0
for b in range(100):
    for m in range(100):
        score += white[b][m]
print(score)        
