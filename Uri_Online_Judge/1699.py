import math 
while(True):
    caso = int(input())
    if caso == 0:
        break
    cont = 0
    num = input().split()
    num = [int(x) for x in num]
    for i in num:
        aux = math.sqrt(i)
        if aux == int(aux):
            cont+=1
        else:
            cont+=2
    if cont%2 == 0:
        print("Garen")
    else:
        print("Annie")
