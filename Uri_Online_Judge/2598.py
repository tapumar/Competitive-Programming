from math import ceil
casos = int(input())
for i in range(casos):
    aven,area = input().split()
    aven = int(aven)
    area = int(area)
    qnt = ceil(aven/area)
    print(qnt)
