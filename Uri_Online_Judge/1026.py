import sys

for linha in sys.stdin:
      A,B = linha.split()
      A = int(A)
      B = int(B)
      A = bin(A)[2:].zfill(32)
      B = bin(B)[2:].zfill(32)
      C = bin(0)[2:].zfill(32)
      x = 31
      while x >=0:
          if A[x] != B[x]:
              list_aux = list(C)
              list_aux[x] = '1'
              C = ''.join(list_aux)
          x = x - 1
      C = int(C,2)
      print (C)
