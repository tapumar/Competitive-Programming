casos = int(input())
for k in range(casos):
  frase = input()
  palavra = input()
  aux = frase.find(palavra)
  nova = ""
  for j in range(len(palavra)):
        nova += "x"
  mark = 0
  while(aux  >= 0):
    if (aux-1<0 or frase[aux-1] == " ") and  (aux+len(palavra)==len(frase) or frase[aux+len(palavra)] == " "):
      if mark == 0:
        print(aux,end="")
      else:
        print(" "+str(aux),end="")
      mark = 1
    frase = frase[:aux] + nova + frase[aux+len(palavra):]
    aux = frase.find(palavra)
  if mark == 0:
    print("-1")
  else:
    print()
 
  frase = frase.replace(nova,palavra)