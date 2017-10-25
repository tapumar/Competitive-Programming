qntTrad = int(input())
trad = {}
for i in range(qntTrad):
  lingua = input().strip()
  t = input().strip()
  trad[lingua] = t
cartas = int(input())
for i in range(cartas):
  crianca = input().strip()
  lingua = input().strip()
  print(crianca)
  print(trad[lingua])
  print()
