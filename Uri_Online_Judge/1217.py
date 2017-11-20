casos = int(input())
totalFrutas = 0
totalPreco = 0.0
for i in range(casos):
    preco = float(input())
    frutas = input().split()
    print("day " + str(i+1) +": " + str(len(frutas))+" kg")
    totalFrutas += len(frutas)
    totalPreco += preco
print("%.2f kg by day" % (totalFrutas/casos))
print("R$ %.2f by day" % (totalPreco/casos))
