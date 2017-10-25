numF,numC = input().split()
numF = int(numF)
numC = int(numC)

tempoF = input().split()
qntC = input().split()
tempo = [0 for x in range(numF)]

i = 0
while(i < numC):
  aux = min(tempo)
  ind = tempo.index(aux)

  tempo[ind] += int(qntC[i])*int(tempoF[ind])
  i += 1
  

print(max(tempo))
    
