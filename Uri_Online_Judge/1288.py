num = int(input().strip())

def descobre(numpro, cargaatual):
  if mat[numpro][cargaatual] != -1:
    return mat[numpro][cargaatual]
  if numpro == proj:
    return 0
    
  if cargaatual+vy[numpro] <= capacidade:
    mat[numpro][cargaatual] = max(descobre(numpro+1, cargaatual), descobre(numpro+1, cargaatual+vy[numpro])+vx[numpro])
  else:
    mat[numpro][cargaatual] = descobre(numpro+1, cargaatual)
    
  return mat[numpro][cargaatual]

for a in range(num):
  proj = int(input().strip())
  vx, vy = ([], [])
  mat = [[-1 for i in range(101)]for j in range(51)]
  for b in range(proj):
    poder, peso = map(int, input().split())
    vx.append(poder)
    vy.append(peso)
    
  capacidade = int(input().strip())
  resistencia = int(input().strip())
  
  
  if descobre(0, 0) >= resistencia:
    print("Missao completada com sucesso")
  else:
    print("Falha na missao")
