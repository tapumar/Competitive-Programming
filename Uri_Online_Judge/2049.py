caso = input().strip("\n")
num = 1
while(caso != "0"):
  if num != 1:
    print()
  seq = input().strip("\n")
  print("Instancia " + str(num))
  if(seq.find(caso)>0):
    print("verdadeira")
  else:
    print("falsa")
  num += 1
  caso = input().strip("\n")
