import sys

for line in sys.stdin:
    line = line.strip("\n")
    auxMin = 0
    auxMai = 0
    auxNum = 0
    ver = True
    if len(line) <6 or len(line) > 32:
      print("Senha invalida.")
    else:
      for i in line:
        if ((ord(i)>122) or (ord(i)<97 and ord(i)>90) or (ord(i)<65 and ord(i)>57) or (ord(i) < 48)):
          print("Senha invalida.")
          ver = False
          break
        if i.islower() == True:
          auxMin = auxMin+1
        elif i.isupper() == True:
          auxMai = auxMai+1
        elif i.isdigit() == True:
          auxNum = auxNum +1
      if ver == True:
        if auxMin>0 and auxNum>0 and auxMai>0:
          print("Senha valida.")
        else:
          print("Senha invalida.")
