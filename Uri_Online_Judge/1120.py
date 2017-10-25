dig,valor = input().split(' ')
while(True):
    if dig=="0" and valor =="0":
        break
    valor = valor.replace(dig,"")
    valor = "".join(valor)
    if valor == "":
      print("0")
    else:
      valor = int(valor)
      print(valor)
    dig,valor = input().split(' ')
