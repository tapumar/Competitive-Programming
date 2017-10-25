j = 0
while(True):
    try:
        j += 1
        sub = input().strip()
        seq = input().strip()
        qnt = seq.count(sub)
        print("Caso #" + str(j) + ":")
        if qnt > 0:
            print("Qtd.Subsequencias: "+ str(qnt))
            teste = seq.replace(sub,"!")
            teste1 = []
            for i in range(len(teste)):
                if teste[i] == "!":
                    teste1.append(i)
            print("Pos: ",end="")
            print(((len(sub)-1)*(qnt-1))+max(teste1)+1)

        else:
            print("Nao existe subsequencia")
        print()
    except EOFError:
        break
