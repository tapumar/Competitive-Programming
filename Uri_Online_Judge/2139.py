import sys

for line in sys.stdin:
  m,d = line.split(' ')
  m = int(m)
  d = int(d)
  if m == 1:
      total = 360
  elif m == 2:
      total = 329
  elif m == 3:
      total = 300
  elif m == 4:
      total = 269
  elif m == 5:
      total = 239
  elif m == 6:
      total = 208
  elif m == 7:
      total = 178
  elif m == 8:
      total = 147
  elif m == 9:
      total = 116
  elif m == 10:
      total = 86
  elif m == 11:
      total = 55
  elif m == 12:
      total = 25
    
  total = total - d
  if total == 1:
      print("E vespera de natal!")
  elif total == 0:
      print("E natal!")
  elif total < 0:
      print("Ja passou!")
  else:
      print("Faltam "+str(total)+" dias para o natal!")
