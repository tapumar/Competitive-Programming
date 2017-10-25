lado = int(input())
cont = 0
while(True):
    if lado<2:
        break
    lado = lado/2
    cont += 1
total = 4    
for j in range(cont-1):
    total = total*4
print(total)
