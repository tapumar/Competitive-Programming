dias,inicial = input().split()
menor = 1001
saldo = int(inicial)
for i in range(int(dias)):
  trans = int(input())
  saldo += trans
  if saldo < menor:
    menor = saldo
print(menor)
