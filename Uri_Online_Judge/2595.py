casos = int(input())

for c in range(casos):
    linhas,colunas,perguntas = input().split()
    linhas = int(linhas)
    colunas = int(colunas)
    perguntas = int(perguntas)
    arena = []
    for l in range(linhas):
        arena.append(input().strip())
    redor = []
    for p in range(perguntas):
        x,y = input().split()
        x = int(x)-1
        y = int(y)-1
        inimigos = 0
        if x > 0 and arena[x-1][y] == "T":
            inimigos += 1
        if x < linhas-1 and arena[x+1][y] == "T":
            inimigos += 1
        if y > 0 and arena[x][y-1] == "T":
            inimigos += 1
        if y < colunas-1 and arena[x][y+1] == "T":
            inimigos += 1
        if x > 0 and y > 0 and arena[x-1][y-1] == "T":
            inimigos += 1
        if x > 0 and y< colunas-1 and arena[x-1][y+1] == "T":
            inimigos += 1
        if x < linhas-1 and y > 0 and arena[x+1][y-1] == "T":
            inimigos += 1
        if x < linhas-1 and y < colunas-1 and arena[x+1][y+1] == "T":
            inimigos += 1
        if inimigos < 5:
            print("GG IZI")
        else:
            print("GRRR")
