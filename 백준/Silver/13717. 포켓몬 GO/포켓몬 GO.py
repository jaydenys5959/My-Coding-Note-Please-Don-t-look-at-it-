x = int(input())
max_num = 0
total = 0

for y in range(x):
    name = input()
    w,n = map(int,input().split())
    count = 0
    while n >= w:
          n -= w
          n += 2 
          count += 1
    total += count
    if count > max_num:
        max_num = count
        max_name = name
print(total)
print(max_name)   