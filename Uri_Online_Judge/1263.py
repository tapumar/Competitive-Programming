while(True):
    try:
        frase = input().split()
        aux = ""
        soma = 0
        mark = 0
        for palavra in frase:
            palavra = palavra.lower()
            if palavra[0] == aux and mark == 0:
                soma += 1
                mark = 1
            elif palavra[0] != aux:
                mark = 0
            aux = palavra[0]
        print(soma)
                    
    except EOFError:
        break
