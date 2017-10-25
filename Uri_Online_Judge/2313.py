import statistics
import math

lados = input().split()
lados = [int(x) for x in lados]

if (abs(lados[0]-lados[1]) < lados[2] and lados[2] < lados[0]+lados[1]) and (abs(lados[0]-lados[2]) < lados[1] and lados[1] < lados[0]+lados[2]) and (abs(lados[2]-lados[1]) < lados[0] and lados[0] < lados[2]+lados[1]):
    print("Valido-",end="")
    if lados[0] == lados[1] and lados[0] == lados[2]:
        print("Equilatero")
    elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
        print("Escaleno")
    else:
        print("Isoceles")
    hip = max(lados)
    cat1 = min(lados)
    cat2 = statistics.median(lados)
    if math.sqrt(((cat1*cat1)+(cat2*cat2))) == hip:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")
