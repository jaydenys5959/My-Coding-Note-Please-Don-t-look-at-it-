ans_burg = 0
ans = 0
high = int(input())
middle = int(input())
low = int(input())
colla = int(input())
saida = int(input())
if high <= middle and high <= low:
    ans_burg = high
elif middle <= high and middle <= low:
    ans_burg = middle
else:
    ans_burg = low
if colla <= saida:
    ans = colla
else:
    ans = saida
X =  ans_burg + ans - 50
print(X)
    
    