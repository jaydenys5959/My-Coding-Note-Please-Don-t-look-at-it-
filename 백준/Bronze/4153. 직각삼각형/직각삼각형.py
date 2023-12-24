while(1):
    A,B,C = map(int,input().split())
    if (A == B == C == 0):
        break
    A2 = A**2
    B2 = B**2
    C2 = C**2

    AB2 = A2 + B2
    BC2 = B2 + C2
    CA2 = C2 + A2
    if (AB2 == C2) or(BC2 == A2) or(CA2 == B2):
        print("right")
    else:
        print("wrong")

    

   

    

   
