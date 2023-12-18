A,B = map(int,input().split())
Q = str(A//B) + "."
A = (A%B) * 10
for i in range(1000):
    Q += str(A//B)
    A = (A%B) * 10
print(Q)