casos = int(input())

for caso in range(casos):
    altura, diametro, galhos = input().split()
    
    altura = int(altura)
    diametro = int(diametro)
    galhos = int(galhos)
    
    if (altura >= 200
        and altura <= 300
        and diametro >= 50
        and galhos >= 150):
        print("Sim")
    else:
        print("Nao")
