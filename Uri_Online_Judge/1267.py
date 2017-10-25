while(True):
    try:
        alunos,jantares = input().split()
        alunos = int(alunos)
        jantares = int(jantares)
        if alunos == 0 and jantares == 0:
            break
        todos = []
        mark = 0
        for i in range(jantares):
            aux = input().split()
            todos.append([int(x) for x in aux])
        for j in range(alunos):
            soma = 0
            for k in range(jantares):
                soma += todos[k][j]
            if soma == jantares:
                print("yes")
                mark = 1
                break
        
        if mark == 0:
            print("no")
            
    except EOFError:
        break
