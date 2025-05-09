N,L = map(int,input().split()) 

cnt = 0 
ans = 0

while True : 
	ans += 1 
	if str(L) not in str(ans) : 
		cnt += 1
		if cnt == N:
			print(ans)
			break	