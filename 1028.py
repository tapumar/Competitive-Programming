casos = int(input())
for i in range(casos):
  n,m = input().split()
  anterior = int(n)
  atual    = int(m)
  resto    = anterior % atual

  while resto != 0:
      anterior = atual
      atual    = resto
      resto    = anterior % atual

  print(atual)
