while(True):
    try:
        
        n = int(input())
        notas = input().split()
        notas = [int(x) for x in notas]
        if notas[1] > notas[0]:
            aux = 1
        else:
            aux = 0
        mark = aux
        picos = 1
        for i in range(1,n):
            if mark == 1 and notas[i] < notas[i-1]:
                picos += 1
                mark = 0
            elif mark == 0 and notas[i] > notas[i-1]:
                picos += 1
                mark = 1
        if mark == 1 and aux == 1:
            picos += 1
        elif mark == 0 and aux == 0:
            picos += 1
        print(picos)
        
    except EOFError:
        break
