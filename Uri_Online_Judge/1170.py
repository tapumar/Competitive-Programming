def metade(num,cont):
  if num<=1:
    return cont
  else:
    cont=cont+1
    return metade(num/2,cont)
    
casos = int(input())

for i in range(casos):
  kilo = float(input())
  tempo = metade(kilo,0)
  print(str(tempo) + " dias")
