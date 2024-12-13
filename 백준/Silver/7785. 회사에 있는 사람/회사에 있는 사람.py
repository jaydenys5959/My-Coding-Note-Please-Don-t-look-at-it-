N = int(input())
a = set() 
for i in range(N):
    A,B = input().split()
    if B == "enter":
        a.add(A)
    else:
        a.remove(A)

a = sorted(a,reverse=True)
for z in a:
    print(z)