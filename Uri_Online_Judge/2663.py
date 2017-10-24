n = int(input())
minimo = int(input())-1
comp = []
for i in range(n):
    comp.append(int(input()))
total = 0   
comp.sort(reverse=True)  
aux = comp[minimo]
for j in comp[minimo+1:]:
    if j != aux:
        break
    total += 1
    
print(minimo+1+total)
