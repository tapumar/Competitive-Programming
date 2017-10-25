while(True):
    try:
        turma = []
        mark = 0
        n,ano = input().split()
        n = int(n)
        for i in range(n):
            nome = input().split()
            novo = "".join([x[0] for x in nome])
            turma.append(novo)
        turmanova = list(set(turma))

        print(len(turma)-len(turmanova))
            
        
    except EOFError:
        break
