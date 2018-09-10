preco, moeda = input().split()
preco = int(preco)
moeda = int(moeda)
preco = preco%500
if moeda >= preco:
    print("Sim")
else:
    print("Nao")
