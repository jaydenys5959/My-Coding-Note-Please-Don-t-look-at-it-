N = int(input())
num = set(map(int,input().split()))
M = int(input())
cards = list(map(int,input().split()))

for i in cards:
    if i in num:
        print(1,end=" ")
    else:
        print(0,end=" ")