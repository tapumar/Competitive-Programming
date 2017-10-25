n = int(input())

for i in range(n):
    frase = input().split()
    ordenada = [] 
    for j in frase:
        mark = 0
        for k in range(len(ordenada)):
            if len(j) <= len(ordenada[k]):
                ordenada.insert(k,j)
                mark = 1
                break
        if mark == 0:
            ordenada.insert(len(ordenada),j)
            
    ordenada = ordenada[::-1]
    for m in range(len(ordenada)):
        if m == 0:
            print(ordenada[m],end="")
        
        else:
            print(" "+ordenada[m],end="")
    print()
