while(True):
    n = int(input())
    if n == 0:
        break
    numeros = input().split()
    pares = []
    for i in numeros:
        if i in pares:
            pares.remove(i)
        else:
            pares.append(i)
           
    print(pares[0])
