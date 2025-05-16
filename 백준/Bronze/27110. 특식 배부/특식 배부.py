N = int(input())
A,B,C = map(int,input().split()) # A는 후라이드 B는 간장 C는 양념❤
ans = 0
D = [A,B,C]
for i in D:
	if i > N:
		ans += N
	elif i <= N:
		ans += i
print(ans)
