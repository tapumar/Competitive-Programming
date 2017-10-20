n = input()
fila = input().split()
m = input()
saiu = input().split()

for i in saiu:
  fila.remove(i)
mark = 0
for j in fila:
  if mark != 0:
    print(" "+j,end="")
  else:
    print(j,end="")
    mark = 1
print()
  
  
