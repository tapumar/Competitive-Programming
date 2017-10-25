while(True):
    try:
        n, ident = input().split()
        n = int(n)
        cont = 0
        for i in range(n):
            autor,jogo = input().split()
            if autor == ident and jogo == "0":
                cont += 1
        print(cont)

    except EOFError:
        break
