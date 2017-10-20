import math
def GCD(a, b):

    if b == 0:
        return a
    else:
        return GCD(b, a % b)
      
while(True):
  try:
    cat = [int(x) for x in input().split()]
    hip = max(cat)
    cat.remove(hip)
    
    if (hip**2) == (cat[0]**2 + cat[1]**2):
      gcd = GCD(cat[0],cat[1])
      gcd = GCD(gcd,hip)
      if gcd == 1:
        print("tripla pitagorica primitiva")
      else:
        print("tripla pitagorica")
    else:
      print("tripla")
  except EOFError:
    break