n = int(input())
lista = []
for i in range(n):
    l = int(input())
    lista.append(l)
    
lista = set(lista)
print(len(lista))
