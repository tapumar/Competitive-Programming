casos = int(input())

for i in range(casos):
    frase1, frase2 = input().split(' ')
    nova = ''
    if len(frase1)<len(frase2):
        for k in range(len(frase1)):
            nova = nova+frase1[0]
            nova = nova+frase2[0]
            frase1 = frase1[1:]
            frase2 = frase2[1:]
        nova = nova+frase2
    else:
        for k in range(len(frase2)):
            nova = nova+frase1[0]
            nova = nova+frase2[0]
            frase1 = frase1[1:]
            frase2 = frase2[1:]
        nova = nova+frase1
    print(nova)
