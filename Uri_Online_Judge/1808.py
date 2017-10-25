texto = input().strip()
total = 0
soma = 0
for i in texto:
    if i == "0":
        total = total+9
    else:     
        nota = int(i)
        total = total+nota
        soma += 1
print('%.2f' % (total/soma))
