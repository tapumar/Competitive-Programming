from math import ceil
f,r = input().split()
gotas = input().split()
maior = 0
f = int(f)
r = int(r)
mark = 0
for i in range(len(gotas)):
  if i == 0:
    if int(gotas[i])-1 > maior:
      maior = int(gotas[i])-1
      mark = 0
  else:
    if ceil((int(gotas[i]) - int(gotas[i-1])-1)/2) > maior:
      maior = ceil((int(gotas[i]) - int(gotas[i-1])-1)/2)
      mark = 1
if f-int(gotas[len(gotas)-1]) > maior:
  maior = f-int(gotas[len(gotas)-1])
  mark = 0
print(maior)
  


