import sys

casos = int(input())
for line in range(casos):
  novaFrase = ""
  line = input().strip()
  num = int(input())
  for i in line:
    n = ord(i)
    if (n >=65 and n<=90):
      n=n-num
      if n<65:
        n = 91-(65-n)
    novaFrase = novaFrase+chr(n)
  print(novaFrase)
