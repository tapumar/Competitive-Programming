num = int(input())

for i in range(num):
    senha = ""
    frase = [x for x in input().split()]
    for j in frase:
        senha = senha + j[0]
    print(senha)
