numeros = input().split()
for i in range(len(numeros)):
    numeros[i] = int(numeros[i])
print(max(numeros))
