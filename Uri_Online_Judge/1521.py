while(True):
    n = int(input())
    if n == 0:
        break
    alunos = input().split()
    alunos = [int(x) for x in alunos]
    primeiro = int(input())
    vez = primeiro-1
    prox = alunos[vez]
    while((vez+1) != prox):
        vez = prox-1
        prox = alunos[vez]
    
    print(vez+1)
