mark = 0
while(True):
    casos = int(input())
    if casos == 0:
        break
    brancP = []
    brancM = []
    brancG = []
    verP = []
    verM = []
    verG = []
    for i in range(casos):
        pessoa = input()
        cor,tamanho = input().split()
        
        if cor == "branco":
            if tamanho == "P":
                brancP.append(pessoa)
            elif tamanho == "M":
                brancM.append(pessoa)
            else:
                brancG.append(pessoa)      
        else:
            if tamanho == "P":
                verP.append(pessoa)
            elif tamanho == "M":
                verM.append(pessoa)
            else:
                verG.append(pessoa)
    if mark != 0:
        print()
    mark = 1
    if len(brancP) > 0:
        brancP.sort()
        [print("branco P",x) for x in brancP]
        
    if len(brancM) > 0:
        brancM.sort()
        [print("branco M",x) for x in brancM]

    if len(brancG) > 0:
        brancG.sort()
        [print("branco G",x) for x in brancG]

    if len(verP) > 0:
        verP.sort()
        [print("vermelho P",x) for x in verP]
    
    if len(verM) > 0:
        verM.sort()
        [print("vermelho M",x) for x in verM]
    
    if len(verG) > 0:
        verG.sort()
        [print("vermelho G",x) for x in verG]
