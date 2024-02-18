A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

ans = 0
if E >= F:
    ans += E
elif E < F:
    ans += F
if A <= B and A <= C and A <= D:
    ans += B+C+D
elif B <= A and B <= C and B <= D:
     ans += A+C+D
elif C <= B and C <= A and C <= D:
     ans += B+A+D
elif D <= B and D <= C and D <= A:
     ans += B+C+A
print(ans)
