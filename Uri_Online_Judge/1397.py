while(True):
    filhos = int(input())
    if filhos == 0:
        break
    p1 = 0
    p2 = 0
    for i in range(filhos):
        valor = input().split()
        if int(valor[0])>int(valor[1]):
            p1 += 1
        elif int(valor[1])>int(valor[0]):
            p2 += 1
    print(p1,p2)
    
