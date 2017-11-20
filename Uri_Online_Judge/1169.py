casos = int(input())

for i in range(casos):
  quad = int(input())
  aux = 1
  graos = 0
  for k in range(quad-1):
    graos = graos+(aux*2)
    aux = aux*2
  peso = (graos/12)/1000
  peso = int(peso)
  print(str(peso) + " kg")
