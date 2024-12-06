ans = ""
N = input()
B = sorted(N,reverse = True)
for i in range(len(N)):
    ans += B[i]
print(ans)
    
