n = int(input())
maior = ["",0,0,0]


for i in range(n):
    cand,poder,matou,morreu = input().split()
    if int(poder) > maior[1]:
        maior = [cand,int(poder),int(matou),int(morreu)]
    elif int(poder) == maior[1]:
        if int(matou) > maior[2]:
            maior = [cand,int(poder),int(matou),int(morreu)]
        elif int(matou) == maior[2]:
            if int(morreu) < maior[3]:
                maior = [cand,int(poder),int(matou),int(morreu)]
            elif int(morreu) == maior[3]:
                mini = min(cand,maior[0])
                if mini == cand:
                    maior = [cand,int(poder),int(matou),int(morreu)]
 
print(maior[0])
