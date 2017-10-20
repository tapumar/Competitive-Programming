casos = int(input())

for i in range(casos):
  tipo = input().strip()
  r,g,b = input().split()
  r = int(r)
  g = int(g)
  b = int(b)
  
  if tipo == "eye":
    p = (0.3*r) + (0.59*g) + (0.11*b)
  elif tipo == "mean":
    p = (r+g+b)/3
  elif tipo == "min":
    p = min(r,g,b)
  else:
    p = max(r,g,b)
  print("Caso #" + str(i+1) + ": " + str(int(p)))
        