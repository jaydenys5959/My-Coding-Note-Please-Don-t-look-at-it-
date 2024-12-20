r = set()
w = set()
ans = []
N,M = map(int,input().split())
for i in range(N):
	A = input()
	r.add(A)
for z in range(M):	
	B = input()
	w.add(B)
ans = list(r & w)
D = len(ans)
ans.sort()
print(D)
for Y in range(D):
    print(ans[Y])