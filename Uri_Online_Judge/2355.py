import math

min = int(input())
while(True):
    if min == 0:
        break
    taxaAlemanha = (min*7)/90
    taxaBrasil = (min*1)/90
    print("Brasil "+ str(math.floor(taxaBrasil))+ " x Alemanha "+str(math.ceil(taxaAlemanha)))
    min = int(input())
