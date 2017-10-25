import math

casos = int(input())

for i in range(casos):
    lado = int(input())
    teste =  lado**2 * 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))
    print('%.3f' % teste)
