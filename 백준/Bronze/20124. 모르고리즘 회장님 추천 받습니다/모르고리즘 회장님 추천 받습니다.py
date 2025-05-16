N =int(input())

name = []
score = 0

for i in range(N):
    A,B = input().split()
    B = int(B)
    if B > score :
        score = B
        name = [A]
    elif B == score :
        name.append(A)
name.sort()
print(name[0])
        