while(True):
    try:
        hab, con = input().split()
        notas = []
        hab = int(hab)
        con = int(con)
        for i in range(hab):
            notas.append(int(input()))
        notas.sort(reverse=True)
        for j in range(con):
            query = int(input())
            print(notas[query-1])

    except EOFError:
        break
