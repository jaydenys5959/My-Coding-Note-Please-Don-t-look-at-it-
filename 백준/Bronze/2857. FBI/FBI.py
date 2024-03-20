check = True
for i in range(5):
    N = input()
    for j in range(len(N)-2):
        if N[j:j+3] == "FBI":
            print(i+1,end = " ")
            check = False
            break
            
if (check):
         print("HE GOT AWAY!") 
