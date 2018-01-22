from math import sqrt

while(True):
  try:
    
    d,vf,vg = input().split()
    d = int(d)
    vf = int(vf)
    vg = int(vg)
    
    t1 = 12/vf
    t21 = 144+(d*d)
    t2 = (sqrt(t21))/vg
    if t1>=t2:
      print("S")
    else:
      print("N")
    
  except EOFError:
    break
