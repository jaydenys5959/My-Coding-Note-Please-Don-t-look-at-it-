N = int(input())
score = list ( map( int, input().split() ) )

max_score = -1

for i in score :
         if max_score < i :
                  max_score = i
                  
total = 0

for i in range(N):
         score[i] = score[i] / max_score * 100
         total += score[i]

print(   total / N ) 