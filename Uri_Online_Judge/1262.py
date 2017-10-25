while(True):
    try:
        ciclo = input().strip()
        processos = int(input())
        soma = 0
        mark = 0
        for i in ciclo:
            if i == "W":
                soma+=1
                mark = 0
            else:
                if mark == 0:
                    soma += 1
                    mark += 1
                elif mark < processos:
                    mark += 1
                else:
                    mark = 1
                    soma += 1
        print(soma)
                    
    except EOFError:
        break
