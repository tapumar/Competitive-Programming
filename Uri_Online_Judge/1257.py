casos = int(input())

for i in range(casos):
    num = int(input())
    soma = 0
    for j in range(num):
        frase = input().strip()
        g = 0
        for k in frase:
            soma += (ord(k)-65) + j + g
            g+=1
    print(soma)
