casos = int(input())

for i in range(casos):
  a,b = input().split(' ')
  tam = len(b)
  essa = "1"
  for j in range(tam):
    essa = essa + "0"
  a = int(a)%int(essa)
  if int(a) == int(b):
    print("encaixa")
  else:
    print("nao encaixa")
