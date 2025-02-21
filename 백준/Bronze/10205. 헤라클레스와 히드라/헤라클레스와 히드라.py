K = int(input())
for i in range(K):
    h = int(input())
    Z = input()
    for D in range(len(Z)):
        if Z[D] == "c":
            h += 1
        elif Z[D] == "b":
            h -= 1
    print("Data Set",str(i+1)+":")
    print(h)
    print(" ")
