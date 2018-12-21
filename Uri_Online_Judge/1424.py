while(True):
    try:
        n, m = input().split()
        m = int(m)
        lista = input().split()
        ind = {}
        for num in range(len(lista)):
            if lista[num] in ind:
                ind[lista[num]].append(num+1)
            else:
                ind[lista[num]] = [num+1]
        for i in range(m):
            k, valor = input().split()
            k = int(k)
            try:
                print(ind[valor][k-1])
            except:
                print(0)
    except:
        break
