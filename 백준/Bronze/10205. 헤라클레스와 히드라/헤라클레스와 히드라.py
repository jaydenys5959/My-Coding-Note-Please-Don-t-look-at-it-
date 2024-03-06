N = int(input())
for i in range(N):
    A = int(input())
    B = input()
    for b in B:
        if (b == "c"):
            A += 1
        else:
            A -= 1
        if A == 0:
            break
    print("Data Set " + str(i+1) + ":")
    print(A)
    print()
