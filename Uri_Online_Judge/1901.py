n = int(input())
floresta = []
achados = []
for i in range(n):
    floresta.append(input().split())
for j in range(2*n):
    x,y = input().split()
    x = int(x)-1
    y = int(y)-1
    if floresta[x][y] not in achados:
        achados.append(floresta[x][y])
print(len(achados))
