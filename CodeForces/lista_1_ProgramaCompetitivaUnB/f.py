n,x = input().split()
a = input().split()
b = input().split()
x = int(x)
aux = 0
for i in a:
    comp = str(x - int(i))
    if comp in b:
        aux = 1
        break
print(aux)
