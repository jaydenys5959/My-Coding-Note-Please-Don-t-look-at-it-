a_point = 0
b_point = 0
last = ""
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in range(len(A)):
    if A[i] > B[i]:
        a_point += 3
        last = "A"
    elif A[i] < B[i]:
        b_point += 3
        last = "B"
    else:
        a_point += 1
        b_point += 1

print(a_point,b_point)
if a_point > b_point:
    print("A")
elif a_point < b_point:
    print("B")
else:
    if last == "A":
        print("A")
    elif last == "B":
        print("B")
    else:
        print("D")
