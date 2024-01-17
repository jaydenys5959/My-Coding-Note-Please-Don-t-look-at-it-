T = int(input()) 
for i in range(T): 
    basket = 0 
    temp = input()
    N = int(input())
    for n in range(N):
        candy = int(input())
        basket += candy
    if basket % N == 0:
        print("YES")
    else:
        print("NO")
    
    
    

