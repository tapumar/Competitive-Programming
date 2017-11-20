n,k = input().split()
while(True):
    if n == "0" and k == "0":
        break
    lista = input().split()
    marc = 0
    for t in range(len(lista)):
        if lista[t] != 0:
            tam = lista.count(lista[t])
            if tam >= int(k):
                marc += 1
                lista = list(map(lambda x: x if x != str(lista[t]) else 0, lista))
        
        
    print(marc)
    
    n,k = input().split()
    
