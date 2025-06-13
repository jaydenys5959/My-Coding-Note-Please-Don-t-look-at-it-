A = 300 #초 단위
B = 60  #초 단위 
C = 10  #초 단위
ans_A = 0
ans_B = 0
ans_C = 0
T = int(input())
Q = [A,B,C]
for i in Q:
    if i == A:
        ans_A += T//A
    elif i == B:
        ans_B += T//B
    else:
        T//C        
        ans_C += T//C
    T = T%i
if T != 0:
    print("-1")
else:
    print(ans_A,ans_B,ans_C)
   
  



        
        
