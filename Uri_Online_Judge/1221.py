from math import sqrt

casos = int(input())

for numero in range(casos):
    num = int(input())
    ehprimo = 1
    for i in range(2,num-1):
        if num%i == 0:
            ehprimo = 0
            break
        if i> sqrt(num):
            break
            
    if ehprimo == 0:
        print("Not Prime")
    else:
        print("Prime")
