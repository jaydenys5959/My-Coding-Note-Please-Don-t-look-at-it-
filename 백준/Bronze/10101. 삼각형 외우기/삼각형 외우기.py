A = int(input())
B = int(input())
C = int(input())
total = A+B+C
if total == 180: 
    if A == 60 and B == 60 and C == 60:
        print("Equilateral")
    elif A == B or A == C or B == C:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Error")
