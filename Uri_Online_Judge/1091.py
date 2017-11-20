while(True):
  casos = int(input())
  if casos == 0:
    break
  divisaX,divisaY = input().split()
  divisaX = int(divisaX)
  divisaY = int(divisaY)
  
  for i in range(casos):
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    
    if X > divisaX and Y > divisaY:
      print("NE")
    elif X > divisaX and Y < divisaY:
      print("SE")
    elif X < divisaX and Y > divisaY:
      print("NO")
    elif X < divisaX and Y < divisaY:
      print("SO")
    else:
      print("divisa")
