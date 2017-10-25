import math

while(True):
    n = int(input())
    if n == 0:
        break
    mark = 0
    aux = int(math.sqrt(n))+1
    for i in range(1,aux):
        if mark == 1:
            print(" ",end="")
        print(i*i,end="")
        mark = 1
    print()
