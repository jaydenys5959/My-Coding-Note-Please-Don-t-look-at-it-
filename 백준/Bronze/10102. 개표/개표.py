V = int(input())
votes = input()

a = 0
b = 0

for v in votes:
    if v == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")