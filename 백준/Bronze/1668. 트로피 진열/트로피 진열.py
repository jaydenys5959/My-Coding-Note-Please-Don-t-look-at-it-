S = []
N = int(input()) 
for i in range(N): 
    A = int(input())
    S.append(A) 

  
left = 0  
left_max = 0

for i in range(N) : 
		if S[i] > left_max :  
			left += 1 
			left_max = S[i] 
			
right = 0  
right_max = 0

for i in range(N-1,-1,-1) :  # 43210
		if S[i] > right_max :  
			right += 1 
			right_max = S[i] 
    
print(left)
print(right)  