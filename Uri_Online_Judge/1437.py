while(True):
    num = int(input())
    if num == 0:
        break
    comandos = input().strip()
    cont = 0
    for i in comandos:
        if i == "D":
            cont+=1
        else:
            cont-=1
    if cont>0:
        if cont%4 == 0:
            print("N")
        elif cont%2 ==0:
            print("S")
        elif cont%3==0:
            print("O")
        else:
            print("L")
    elif cont < 0:
        if cont%4 == 0:
            print("N")
        elif cont%2 ==0:
            print("S")
        elif cont%3==0:
            print("L")
        else:
            print("O")
    else:
        print("N")
