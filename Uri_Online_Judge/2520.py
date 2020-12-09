while(True):
    try:
        n, m = input().split()
        pos_l1 = 0
        pos_c1 = 0
        pos_l2 = 0
        pos_c2 = 0
        for linha in range(int(n)):
            colunas = input().split()
            if '1' in colunas:
                pos_c1 = int(colunas.index('1'))
                pos_l1 = int(linha)
            if '2' in colunas:
                pos_c2 = int(colunas.index('2'))
                pos_l2 = int(linha)
        distancia = abs(pos_l1-pos_l2) + abs(pos_c1-pos_c2)
        print(distancia)
    except EOFError:
        break
