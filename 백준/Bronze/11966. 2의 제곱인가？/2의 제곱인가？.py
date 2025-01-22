N = int(input())
A = []
for i in range(31):
    A.append(2**i)
if N in A:
    print("1")
else:
    print("0")
