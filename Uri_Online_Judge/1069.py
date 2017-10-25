casos = int(input())

for i in range(casos):
    linha = input().strip()
    linha = linha.replace(".","")
    aux = linha
    soma = 0
    while(True):
        soma += linha.count("<>")
        linha = linha.replace("<>","")
        if aux == linha or len(linha) == 0:
            break
        else:
            aux = linha
        
    print(soma)
