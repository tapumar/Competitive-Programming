while(True):
    casos = int(input())
    if casos == 0:
        break
    primeiroPlaneta = ""
    menorTempo = 2200
    for i in range(casos):
        planetas = input().split()
        if (int(planetas[1])-int(planetas[2])) < menorTempo:
            primeiroPlaneta = planetas[0]
            menorTempo = int(planetas[1])-int(planetas[2])
    print(primeiroPlaneta)
