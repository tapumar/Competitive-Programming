pontos = input().split()
pontos = [float(x) for x in pontos]

maior = min(pontos)

if pontos[0] < pontos[1] and pontos[0] < pontos[2]:
    print("Otavio")
elif pontos[1] < pontos[0] and pontos[1] < pontos[2]:
    print("Bruno")
elif pontos[2] < pontos[1] and pontos[2] < pontos[0]:
    print("Ian")
else:
    print("Empate")
