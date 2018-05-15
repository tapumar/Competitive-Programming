pratos = input().split()
pedidos = input().split()
total = 0
for x in range(3):
    if int(pedidos[x]) > int(pratos[x]):
        total += int(pedidos[x])-int(pratos[x])
print(total)
