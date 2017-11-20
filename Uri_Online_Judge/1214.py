casos = int(input())

for i in range(casos):
  soma = 0
  alunos = input().split()
  del alunos[0]
  
  for j in alunos:
    soma = soma+int(j)
  soma = soma/len(alunos)
  
  alunos1 = [x for x in alunos if int(x) > soma]
  print('%.3f' % ((len(alunos1)*100.0)/len(alunos)) + "%")
