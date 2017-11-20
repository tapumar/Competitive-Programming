while(True):
    filhos = input().split()
    if filhos[0]=="0" and filhos[1]=="0":
        break
    soma = int(filhos[0]) + int(filhos[1])
    print(soma)
