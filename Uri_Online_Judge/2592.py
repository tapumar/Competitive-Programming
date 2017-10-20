n = int(input())
while(True):
  if n == 0:
    break
  tamanho = 0
  while(True):
    teste = input().split()
    if len(teste) != n:
      n = int(teste[0])
      break
    tamanho += 1
  print(tamanho)
    