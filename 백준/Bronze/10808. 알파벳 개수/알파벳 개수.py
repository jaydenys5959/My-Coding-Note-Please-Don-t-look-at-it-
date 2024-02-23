a=input()
ls=[0]*26

for i in a:  
    ls[ord(i)-97]=a.count(i)
for i in ls:
    print(i, sep=' ')