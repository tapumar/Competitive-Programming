notas = input().split()
total = 0
notas = list(map(float, notas))
maior = max(notas)
menor = min(notas)
del notas[notas.index(maior)]
del notas[notas.index(menor)]
for i in notas:
    total += i
print('%.1f' % total)
