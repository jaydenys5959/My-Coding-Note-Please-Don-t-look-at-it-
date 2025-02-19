d = 0
a = []
for i in range(8):
    N = input()
    a.append(N)
for i in range(8):
    for z in range(8):
        if a[i][z] == "F":
            if (z % 2 == 0 and i % 2 == 0) or (z % 2 == 1 and i % 2 == 1):
                d += 1
            
print(d)  

