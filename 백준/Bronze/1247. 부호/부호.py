for V in range(3):
    N = int(input())
    S = 0
    for i in range(N):
        A = int(input())
        S += A
    if S == 0:
        print("0")
    elif S > 0:
        print("+")
    else:
        print("-")
