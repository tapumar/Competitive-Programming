troca1 = []
troca2 = []
nova = ""
qtd_letras, qtd_frases = input().split()
qtd_letras = int(qtd_letras)
qtd_frases = int(qtd_frases)
for i in range(qtd_letras):
    certa, errada = input().split()
    troca1.append(certa)
    troca2.append(errada)

for j in range(qtd_frases):
    nova = ""
    frase = input()
    for i in frase:
        if i in troca1:
            ind = troca1.index(i)
            nova += troca2[ind]
        elif i in troca2:
            ind = troca2.index(i)
            nova += troca1[ind]
        else:
            nova += i
    print(nova)
