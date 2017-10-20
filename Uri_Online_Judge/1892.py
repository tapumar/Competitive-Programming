while(True):
  n = int(input())
  mats = []
  soma = 0
  for i in range(n):
    aux = input().strip()
    mats.append(int(aux.replace("/","")))
    
  for j in mats:
    aux = mats[mats.index(j)+1:]
    teste = [x for x in aux if x<j]
    #while(j != max(aux)):
    #  aux.remove(max(aux))
    #soma += len(aux)-1
  print(len(teste))
  