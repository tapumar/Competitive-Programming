import math
casos = int(input())
for i in range(casos):
    num = int(input())  
    soma = 0
    for j in range(1,num+1):
        aux = math.sqrt(j)
        if aux == int(aux):
            soma += 1
             
    print(num-soma)
