casos = int(input())
for i in range(casos):
    num = int(input())
    aux = ""
    cont = 0
    for j in range(num):
        pessoa = input().strip()
        if pessoa != aux:
            cont = cont+1
        aux = pessoa
    if cont > 1:
        print("ingles")
    else:
        print(aux)
            
