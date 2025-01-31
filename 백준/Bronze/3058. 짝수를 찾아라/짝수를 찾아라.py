T = int(input())
for i in range(T):
    d = []
    w = 0
    min_ = 101 
    A = list(map(int,input().split()))
    for z in range(len(A)):
        if A[z] % 2 == 0: #짝수
            d.append(A[z])#짝수 총 리스트    
    for m in range(len(d)):
        w += d[m] # 짝수 합
        if d[m] < min_:
            min_ = d[m]
    print(w,min_)
