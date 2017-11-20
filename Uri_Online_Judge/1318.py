while(True):
  original, festa = input().split()
  if original == "0" and festa == "0":
    break
  bilhetes = input().split()
  teste = [x for x in bilhetes if bilhetes.count(x) > 1]
  teste = set(teste)
  teste = list(teste)
  print(len(teste))
    
