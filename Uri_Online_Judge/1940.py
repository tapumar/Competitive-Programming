jogadores, rodadas = input().split()
jogadores = int(jogadores)
rodadas = int(rodadas)
total = [0]*jogadores
pontos = input().split()
j = 0
for i in range(len(pontos)):
    if j == jogadores:
        j = 0
    total[j] += int(pontos[i])
    j += 1
maior = max(total)
todos = [k for k in range(len(total)) if total[k]== maior]
print(max(todos)+1)
