caso = 1
while(True):
    try:
        num = input().strip()
        caixa = input().split()
        totalF = 0
        totalM = 0
        for i in range(len(caixa)):
            if caixa[i] == num:
                if caixa[i+1] == "F":
                    totalF += 1
                else:
                    totalM += 1
        if caso != 1:
            print()
        print("Caso "+ str(caso)+":")
        print("Pares Iguais: "+ str(totalF+totalM))
        print("F: "+str(totalF))
        print("M: "+str(totalM))

        caso += 1
    except EOFError:
        break
