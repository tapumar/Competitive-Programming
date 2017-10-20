n,q = input().split()
n = int(n)
q = int(q)
mat = [[0] * n for i in range(n)]
print(mat)
for i in range(q):
  ope = input().split()
  if ope[0] == "1":
    x = int(ope[1])-1
    r = int(ope[2])
    mat[x] = [r] * n
    print(mat)
  elif ope[0] == "2":
    x = int(ope[1])-1
    r = int(ope[2])
    for k in range(n):
      mat[k][x] = r
    print(mat)
  #elif ope[0] == "3":
  #else:
    
  
  