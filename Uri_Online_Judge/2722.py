casos = int(input())

for i in range(casos):
    linha1 = input()
    linha2 = input()
    nome = ""
    for letra in range(len(linha1)):
        if letra%2 == 0:
            nome += linha1[letra] + linha1[letra+1] + linha2[letra]
            try:
                nome += linha2[letra+1]
            except:
                break
    print(nome)
