N = int(input())
for i in range(N):
    A,B,C,D,E = map(int,input().split())
    S = 350.34 * A
    Q = 230.90 * B
    O = 190.55 * C
    L = 125.30 * D
    R = 180.90 * E
    Z = S+Q+O+L+R
    total = Z
    print(f"${'%.2f'%total}")
