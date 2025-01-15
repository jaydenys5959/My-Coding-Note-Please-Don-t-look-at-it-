n = int(input())
k = 1
ans = 0 
while n > 0 :
	n -= k
	k += 1
	if k > n:
		k = 1
	ans += 1 
	
print(ans)
