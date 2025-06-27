N = int(input())
for i in range(N):
    A = list(map(int,input().split()))[1:]
    B = list(map(int,input().split()))[1:]
    count_A = [0,0,0,0,0]
    count_B = [0,0,0,0,0]
	
    for a in A : 
        count_A[a] += 1   
			
    for b in B :
        count_B[b] += 1
    for j in range(4,-1,-1):
        if j == 0 : 
            print("D") 
        if count_A[j] > count_B[j] :
            print("A")
            break 
        elif count_A[j] < count_B[j] :
            print("B") 
            break 
