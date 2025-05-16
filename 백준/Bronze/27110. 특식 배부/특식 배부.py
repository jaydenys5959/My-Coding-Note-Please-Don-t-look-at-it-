N = int(input())
A,B,C = map(int,input().split()) # A는 후라이드 B는 간장 C는 양념❤

ans = min(A,N) + min(B,N) + min(C,N)

print(ans)