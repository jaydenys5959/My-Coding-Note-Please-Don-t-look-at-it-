a = int(input()) # 테스트 케이스 개수
for z in range(a): # 테스트 케이스 반복
    w = 0 
    s = int(input()) # 자동차 가격
    w += s
    n = int(input()) # 옵션 몇 개
    for i in range(n): #옵션 n 만큼 반복
        q,p = map(int,input().split())
        w += q*p
    print(w)
    