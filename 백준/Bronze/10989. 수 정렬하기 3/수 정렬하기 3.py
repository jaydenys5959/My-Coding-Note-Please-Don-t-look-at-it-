N = int(input())
com = [0] * 10001
for i in range(N):
    A = int(input())
    com[A] += 1
for s in range(10001):
    if com[s] != 0:
        for w in range(com[s]):
            print(s)

        
