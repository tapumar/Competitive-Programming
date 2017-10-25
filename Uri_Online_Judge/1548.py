casos = int(input())
for i in range(casos):
    qntAlunos = int(input())
    notasAlunos = input().split()
    notasAlunos = [int(x) for x in notasAlunos]
    changed = True
    aux = notasAlunos
    notasAlunos = sorted(notasAlunos,reverse=True)
    soma = 0
    for x in range(len(notasAlunos)):
        if notasAlunos[x] == aux[x]:
            soma += 1
            
    print(soma)
