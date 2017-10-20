festaSim = []
festaNao = []
maiorP = ""
maior = 0
while(True):
  pessoa = input().split()
  if pessoa[0] == "FIM":
    break
  if pessoa[1] == "YES":
    if len(pessoa[0]) > maior:
      maior = len(pessoa[0])
      maiorP = pessoa[0]
    if pessoa[0] not in festaSim:
      festaSim.append(pessoa[0])
  else:
    if pessoa[0] not in festaNao:
      festaNao.append(pessoa[0])
festaSim.sort()
festaNao.sort()
[print(x) for x in festaSim]
[print(x) for x in festaNao]
print()
print("Amigo do Habay:")
print(maiorP)
    