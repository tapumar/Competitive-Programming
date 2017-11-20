casos = int(input())

for i in range(casos):
    nova = ""
    invert = ""
    inicio,fim = input().split()
    for j in range(int(fim)-int(inicio)+1):
        aux = int(inicio)+j
        nova = nova + str(aux)
    invert = nova[::-1]
    print(nova+invert)
