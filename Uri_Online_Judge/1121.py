while(True):
    try:
        
        linhas,colunas,inst = input().split()
        arena = []
        linhas = int(linhas)
        colunas = int(colunas)
        soma = 0
        mark = 1
        aux = 0
        iniL = 0
        iniC = 0
        for i in range(linhas):
            arena.append(input())
            
            if "N" in arena[i]:
                aux = 1
                iniL = i
                iniC = arena[i].index("N")
            elif "L" in arena[i]:
                aux = 2
                iniL = i
                iniC = arena[i].index("L")
            elif "S" in arena[i]:
                aux = 3
                iniL = i
                iniC = arena[i].index("S")
            elif "O" in arena[i]:
                aux = 4
                iniL = i
                iniC = arena[i].index("O")
        caminho = input().strip()
        for k in caminho:
            if k == "D":
                aux = aux + 1
                if aux > 4:
                    aux = 1
            elif k == "E":
                aux = aux - 1
                if aux < 1:
                    aux = 4
            else:
                if aux == 1 and iniL > 0 and arena[iniL-1][iniC] != "#":
                    iniL -= 1
                elif aux == 2 and iniC < (colunas-1) and arena[iniL][iniC+1] != "#":
                        iniC += 1
                elif aux == 3 and iniL < linhas-1 and arena[iniL+1][iniC] != "#":
                    iniL += 1
                elif aux == 4 and iniC > 0 and arena[iniL][iniC-1] != "#":
                    iniC -= 1
                    
                if arena[iniL][iniC] == "*":
                    soma += 1
                    mark = arena[iniL][iniC+1:]
                    arena[iniL] = arena[iniL][:iniC] + "." + mark
                                        
        print(soma)
    except EOFError:
        break
