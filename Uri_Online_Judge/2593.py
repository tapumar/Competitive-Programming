frase = input()
qnt = int(input())
palavras = input().split()

for i in palavras:
  aux = frase.find(i)
  nova = ""
  for j in range(len(i)):
        nova += "x"
  mark = 0
  while(aux  >= 0):
    if (aux-1<0 or frase[aux-1] == " ") and  (aux+len(i)==len(frase) or frase[aux+len(i)] == " "):
      if mark == 0:
        print(aux,end="")
      else:
        print(" "+str(aux),end="")
      mark = 1
    frase = frase[:aux] + nova + frase[aux+len(i):]
    aux = frase.find(i)
  if mark == 0:
    print("-1")
  else:
    print()
 
  frase = frase.replace(nova,i)
      