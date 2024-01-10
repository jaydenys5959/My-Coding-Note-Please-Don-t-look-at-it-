c = int(input())
score = list(map(int,input().split()))
max_ = -1
min_ = 1001
    
for i in range(c):
    if max_ < score[i]:
        max_ = score[i]
    if min_ > score[i]:
        min_ = score[i]
print(max_ - min_)        
