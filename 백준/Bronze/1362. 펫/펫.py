적정=0
실제 = 0
시나리오 = 1
signal = True
while True:
    
    a,s =input().split()
    if a == "0" and s == "0":
        break
    elif a == "#":
        if  적정 * 0.5 < 실제 < 적정 * 2 and signal :
            print(시나리오,':-)')
        elif 실제 <= 0 or not(signal):
            print(시나리오,"RIP")
        else:
            print(시나리오,":-(")
        시나리오 += 1
        signal = True
    elif a == "F":
        실제 += int(s)

    elif a == "E":
        실제 -= int(s)	
        if 실제 <= 0:
            signal = False
    else:
        실제 = int(s)
        적정 = int(a)
