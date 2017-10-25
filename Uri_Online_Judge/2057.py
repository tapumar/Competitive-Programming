saida,tempo,fuso = input().split()
saida = int(saida)
tempo = int(tempo)
fuso = int(fuso)

chegada = saida + tempo + fuso
if chegada > 23:
    chegada = chegada - 24
if chegada < 0:
    chegada = 24 + chegada

print(chegada)
