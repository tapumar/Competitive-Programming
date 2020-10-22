import sys

def fat(num):
  if num <2:
    return 1
  else:
    return num*fat(num-1)
for line in sys.stdin:
  num1,num2 = line.split(' ')
  num1= int(num1)
  num2= int(num2)

  soma = fat(num1) + fat(num2)
  print(soma)
