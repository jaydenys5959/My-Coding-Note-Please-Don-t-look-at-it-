t = int(input())
G_score = [1,2,3,3,4,10]
S_score = [1,2,2,2,3,5,10]
for i in range(t):
    G = list(map(int,input().split()))
    S = list(map(int,input().split()))
    G_TOTAL= 0
    S_TOTAL= 0
    for j in range(6):
             G_TOTAL += G_score[j] * G[j]
    for O in range(7):
             S_TOTAL += S_score[O] * S[O]
    if G_TOTAL > S_TOTAL:
        print("Battle " + str(i+1) + ":" +  " Good triumphs over Evil")
    elif G_TOTAL == S_TOTAL:
        print("Battle " + str(i+1) + ":" +" No victor on this battle field")
        
    else:
        print("Battle " + str(i+1) + ":" + " Evil eradicates all trace of Good")
