
while(True):
   n = input().strip()
   if n == "-1":
       break
   precos = input().split()
   ingressos = 0
   idas = 0
   for i in precos:
       ingressos += int(i)   
       if ingressos%100 == 0 and ingressos != 0:
           idas += 1
           ingressos = 0
   print(idas)
