letra = input().strip()
texto = input().split()
cont = 0
for palavra in texto:
    if palavra.find(letra) >= 0:
        cont += 1
total = (cont*100)/len(texto)
print('%.1f' % total)
