n, maior, trans = input().split()
trans = int(trans)
maior = int(maior)
n = int(n)
pris = input().split()
qtd = 0
fila = 0

for i in pris:
    if int(i) <= maior:
        qtd += 1
    else:
        if qtd >= trans:
            fila += (qtd-trans+1)
        qtd = 0
if qtd >= trans:
    fila += (qtd-trans+1)
print(fila)
