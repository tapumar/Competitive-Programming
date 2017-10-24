import operator

while(True):
    try:
        n = int(input())
        carnes = {}
        for i in range(n):
            aux = input().split()
            carnes[int(aux[1])] = aux[0]
        sorted_x = sorted(carnes.items(), key=operator.itemgetter(0))
        aux = 1
        for i in sorted_x:
            if aux == len(sorted_x):
                print(i[1])
            else:
                print(i[1],end=" ")
            aux += 1

    except EOFError:
        break
