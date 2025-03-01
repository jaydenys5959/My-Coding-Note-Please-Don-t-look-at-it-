c = int(input())

for c in range(c):
    info = list(map(int,input().split()))
    N = info[0]
    total = 0
    for i in range(1,N+1):
        total += info[i]
    avg = total/N
    count = 0
    for i in range(1,N+1):
        if avg < info[i]:
            count += 1
    rate = count/N * 100
    print(f'{rate:.3f}%')