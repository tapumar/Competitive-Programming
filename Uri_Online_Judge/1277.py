casos = int(input())
for i in range(casos):
    numEst = int(input())
    estudantes = input().split()
    registros = input().split()
    tam = len(registros)
    mark = 0
    for j in range(tam):
        registros[j] = registros[j].replace("M","")
        tam1 = len(registros[j])
        qntP = registros[j].count("P")
        freq = (qntP*100)/tam1
        if freq < 75:
            if mark == 1:
                print(" "+estudantes[j],end="")
            else:
                print(estudantes[j],end="")
                mark = 1
    print()
