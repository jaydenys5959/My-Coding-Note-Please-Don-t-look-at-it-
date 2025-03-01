word = input().upper()
count = [0]*26

for i in word:
    count[ord(i) - 65] += 1
    
idx = 0
ans = "A"

for i in range(1,26):
    if(count[i] > count[idx]):
        idx = i
        ans = chr(idx + 65) # chr(65) ->"A"
    elif (count[i] == count[idx]):
        ans = "?"
print(ans)
