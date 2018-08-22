n,m = input().split()
n = int(n)
m = int(m)
c = input().split()
plat = [0]*n
for i in c:
    i = int(i)
    plat[i-1] = plat[i-1] + 1
min = min(plat)
for x in range(len(plat)):
    plat[x] = plat[x] - min
print(min)
