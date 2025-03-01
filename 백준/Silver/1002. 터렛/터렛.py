for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2: 
        if r1 == r2:
            print(-1)

        else: 
            print(0)

    else:
        d = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5) 
    
        if d == r1 + r2 or d == abs(r2 - r1): 
            print(1)

        elif abs(r2 - r1) < d < r1 + r2:
            print(2)

        else: 
            print(0)