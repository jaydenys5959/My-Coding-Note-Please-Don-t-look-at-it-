N = int(input())
ans = 1001
for i in range(N):
    A,B = map(int,input().split())

    if A <= B: # 내가 빵을  살 수 있는 경우라면,
        if B < ans:
            ans = B         
if 1001 == ans:
    print(-1)
else:
    print(ans)
        
    
 