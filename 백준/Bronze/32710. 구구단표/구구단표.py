b = 1
c = 1
N = int(input())
for a in range(2,10):
   for s in range(1,10):
       C = a*s
       if N == a or N == s or N == C:
           print("1")
           exit()
print("0")
       
  
