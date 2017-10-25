import operator

carros,voltas = input().split()
carros = int(carros)
voltas = int(voltas)
maior = {}
for i in range(carros):
    soma = 0
    t = input().split()
    for k in t:
        soma += int(k)
    maior[i+1] = soma
sorted_x = sorted(maior.items(), key=operator.itemgetter(1))
print(sorted_x[0][0])
print(sorted_x[1][0])
print(sorted_x[2][0])
